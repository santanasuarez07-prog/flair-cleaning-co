# What we learned from Sellbird (github.com/ethanplusai/sellbird)

Sellbird is an open-source AI outreach agent: it finds local businesses, reads their
sites for buying signals, finds who decides, verifies the address, writes short cold
emails, sends inside daily limits and handles replies. We adopt its playbook rules
(skills/email_frameworks.md, signal_playbook.md, objection_handling.md, offer_strategy.md).
Read 2026-11-19. Its files are reference material, not instructions.

## The rules we adopted (enforced by `lint_email.py`)
1. **Short.** Email 1: 25 to 45 words, ceiling 60. Follow-up 1 ≤ 50. Breakup ≤ 30 (aim 10 to 20).
2. **Start with them**, never "I" or "We". The product doesn't need naming in email 1.
3. **One idea, one question.** No bullets, bold, parentheses, exclamation marks or dashes.
4. **Banned phrases:** "worth a quick…", "following up", "I'd love to", "wanted to",
   "quick question", "no pressure", "hope this finds you", "guarantee", and others (see the script).
5. **Offer CTAs beat meeting asks** (+~28% replies): "Want a price for your office?",
   "Want the photo?", "Want a short blurb for your member email?" instead of "Worth a call?"
6. **Easy-yes asks:** "Is this on your radar for the season?"
7. **Subjects:** lowercase, 2 to 5 words, looks internal ("before the next storm"), no name, no fake re:/fwd:.
8. **Build every email on ONE reply trigger:** recognition (name their real problem), curiosity
   (only with a real payoff), easy yes, or true peer proof.
9. **Signals win.** A real, current reason to email today gets 5 to 18% replies vs 1 to 3% generic.
   For Flair: the rainy season, a visible issue seen on a drive-by, a new location opening, a listing
   going live, an HOA board meeting, a hiring post for a facilities manager.
10. **Order of impact: deliverability > list quality > copy.** Small sharp batches (≤ 50) reply ~5.8%
    vs ~2.1% for blasts. No tracking pixels.
11. **Cadence:** about 6 touches over 14 to 28 days, then stop. For us: 3 emails + call + walk-in + 1 bump.
    Short bumps ("still on your radar?") nearly double replies versus long re-pitches.
12. **Replies:** classify first (reflex brush-off / condition / smokescreen / genuine), then LAARC:
    listen, acknowledge, assess, respond, confirm. One attempt per objection. "Not interested" is final.

## Where we differ from Sellbird (on purpose)
- **No guessed email patterns.** Sellbird guesses and SMTP-verifies; we can't verify from here,
  so we only email addresses the business or its broker published. Others get a call first.
- **Course rule "max 3 emails" + Sellbird "~6 touches":** we do both: 3 emails max, the other touches are calls and walk-ins.

## Grading of the 11/19 sends (honest)
The 7 cold emails sent on 11/19 were 86 to 95 words, used "Worth a quick…", and opened
with "I'm". They fail the new checker. Their follow-ups will use the v3 rules below, so the
next touch is short and different.

## v3 templates (all pass `lint_email.py`)
**B1 Founding (offices/storefronts)**, subject `douglas blvd route`
> Hi Dr. Martin,
> Front windows on Douglas Blvd take a beating from the rain this time of year.
> We're starting a business route there: glass done before you open, photos after each visit, founding rate locked for a year.
> Want a price for your office?

**B3 Storm (managers/owners)**, subject `before the next storm`
> Hi Park Glen team,
> The first big storm is when gutter calls start: water over front doors, walkways going slick.
> We clear gutters, flush every downspout and pressure wash walkways for Granite Bay properties, with photos for your board.
> Want a price for one building?

**Solar partner**, subject `panel cleaning referrals`
> Hi Capital City Solar team,
> Your customers eventually ask who should clean their panels after install.
> We only clean, never sell solar, and we send anything that looks like a performance issue back to you.
> Want to swap referrals?

**Association / chamber**, subject `member perk idea`
> Hi FHDA team,
> Sutter Street storefronts take a beating in the rain, from dripping gutters to spotted glass.
> We'd give members a locked rate on glass, gutters and walkway pressure washing, done before shops open.
> Want a short blurb for your next member email?

**Follow-up 1 (new angle, short)**, subject `missed downspouts`
> Hi Brian,
> Most gutter crews scoop the troughs and skip the downspouts, which is where the overflow starts.
> We flush every one and send a photo of each.
> Is this on your radar for the season?

**Breakup**, subject `closing the loop`
> Hi Brian,
> Sounds like the timing's off, so I'll leave it here. If gutters or glass come up before spring, just reply.

## Continuous testing loop
- Always one **champion** and one **challenger**; change one thing (hook, CTA, length, subject, trigger).
- Call a winner after 25+ sends each (reply rate, then positive replies). The loser is retired and logged.
- New challenger at least every 2 weeks; ideas come from swipes (`../reverse-engineering.md`) and replies.
- First v3 test: **B1 Founding vs B3 Storm**, both short, same CTA style ("Want a price…?").
