#!/usr/bin/env python3
"""Pre-send check for Flair cold emails (rules adapted from Sellbird's email_frameworks
playbook + our own). Usage:
  python3 lint_email.py --touch 1 --subject "subject" --body-file email.txt
  python3 lint_email.py --selftest
Exit code 0 = pass, 1 = fix before sending. The footer (from 'Santana Suarez' down) is ignored.
"""
import argparse, re, sys

LIMITS = {1: 60, 2: 50, 3: 30}          # hard ceilings (Sellbird); aim 25-45 for touch 1
TARGET = {1: (25, 45), 2: (15, 40), 3: (8, 20)}
BANNED = ["picture this", "here's what i keep", "worth a quick", "i hope this finds you",
          "just following up", "following up", "i'd love to", "in today's", "imagine if",
          "what if i told you", "game-changer", "game changer", "revolutionary", "cutting-edge",
          "let me know if you're interested", "are you the right person", "reaching out because",
          "just wanted to", "wanted to", "no pressure", "no obligation", "quick question",
          "act now", "free money", "guarantee", "just checking in", "touch base", "circle back"]

def body_only(text):
    cut = re.split(r"\n\s*Santana Suarez\s*\n", text, maxsplit=1)
    return cut[0].strip()

def words(t):
    return re.findall(r"[A-Za-z0-9$'+%.]+", t)

def lint(subject, text, touch=1):
    issues, body = [], body_only(text)
    lines = [l for l in body.splitlines() if l.strip()]
    # drop a greeting line like "Hi Brian," from the count of openers
    content = lines[1:] if lines and re.match(r"^(hi|hey|hello)\b.*,$|^[A-Z][a-z]+,$", lines[0], re.I) else lines
    n = len(words(" ".join(content)))
    lo, hi = TARGET[touch]
    if n > LIMITS[touch]: issues.append(f"too long: {n} words (ceiling {LIMITS[touch]}, aim {lo}-{hi})")
    elif n > hi: issues.append(f"long-ish: {n} words (aim {lo}-{hi})")
    low = body.lower()
    for b in BANNED:
        if b in low: issues.append(f'banned phrase: "{b}"')
    if re.search(r"[–—]| - ", body): issues.append("dash between words (em/en dash or spaced hyphen)")
    if "!" in body: issues.append("exclamation mark")
    if re.search(r"^\s*([-*•]|\d+\.)\s", body, re.M): issues.append("bullet or numbered list")
    if re.search(r"\([^)]*\)", body): issues.append("parenthetical aside")
    if content and re.match(r"^(i|i'm|i've|we|we're|our)\b", content[0].strip(), re.I):
        issues.append("opens with I/We (start with them)")
    q = body.count("?")
    if q == 0 and touch < 3: issues.append("no question / ask")
    if q > 1: issues.append(f"{q} questions (pick one)")
    if len(re.findall(r"https?://|www\.", body)) > (0 if touch == 1 else 1): issues.append("too many links")
    s = subject.strip()
    if s != s.lower(): issues.append("subject not lowercase")
    if not 2 <= len(s.split()) <= 5: issues.append(f"subject is {len(s.split())} words (2-5)")
    if re.match(r"^(re|fwd?):", s, re.I) and touch == 1: issues.append("fake re:/fwd: subject")
    if "quick question" in s.lower(): issues.append('subject uses "quick question"')
    if "won't email again" not in text.lower(): issues.append("missing opt-out footer")
    if "8687 willow valley" not in text.lower(): issues.append("missing physical address (CAN-SPAM)")
    return n, issues

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", default=""); ap.add_argument("--body-file"); ap.add_argument("--touch", type=int, default=1)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        good = ("Hi Brian,\n\nRain season is when center walkways turn green and slick by the storefront doors.\n\n"
                "We keep glass, gutters and walkways clean for Roseville properties, photos after every visit.\n\n"
                "Want a price for one of yours?\n\nSantana Suarez\nOwner, Flair Cleaning Co\n(916) 234-8343 | flaircleaningcompany.com\n"
                "8687 Willow Valley Place, Granite Bay, CA 95746\nNot a fit? Reply \"no thanks\" and I won't email again.")
        n, iss = lint("walkways at your centers", good, 1); print("good:", n, iss or "PASS")
        assert not iss, iss
        n, iss = lint("Quick question, Brian", "I'm Santana - worth a quick look? Really!", 1)
        print("bad:", n, iss); assert iss
        return
    text = open(a.body_file).read()
    n, iss = lint(a.subject, text, a.touch)
    print(f"{n} words"); print("PASS" if not iss else "FIX:\n  - " + "\n  - ".join(iss))
    sys.exit(1 if iss else 0)

if __name__ == "__main__":
    main()
