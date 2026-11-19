# Flair Cleaning Co: Marketing Playbook

## Positioning
**"The exterior of your home, done right, without you lifting a finger."**
Local, owner-operated, insured, fast quotes (same day, no site visit), easy
scheduling, you don't need to be home for exterior work.

Proof points to reuse: streak-free hand-finished glass, every downspout
flushed, gentle soft-wash (no blasted paint), solar cleaned without damaging
panels, real person answers texts.

## Voice
Friendly, confident, a little playful (our "neighbors a little jealous" and
"glow-up" messages land well). Plain words, short sentences, one emoji max.
Sign as "Flair" or "Flair Cleaning Co". Never pushy; always a soft out.

## Segments (build in Flyra with `flyra_filter_customers` and tags)
| Segment | Flyra filter | Main play |
|---|---|---|
| **New leads** | lead.created | 5-touch nurture (speed-to-lead) |
| **Quoted, not booked** | pipeline stage "Quoted No Cleaning" | objection rescue + smaller first step |
| **One-time customers, 0 to 5 mo** | job_count=1 | referral ask → cross-sell |
| **Due for rebook** | last_booked_days_gt 150 | rebook reminder, "same price as last time" |
| **Lapsed 180+ days / never booked** | last_booked_days_gt 180 or job_count=0 | win-back with a bonus add-on |
| **Recurring (quarterly / bi-annual)** | has_subscription=true | VIP: early access, referral bonus; never discount-blast them |
| **Solar owners** | bought Solar Panel Cleaning | spring pollen + summer output messages |
| **High LTV** | min_lifetime_value_cents 60000 | personal text from owner, plan upsell |

**Tag plan (to create on approval):** `solar-owner`, `gutters`, `windows`,
`pressure-wash`, `recurring`, `vip`, `referral-source`, `b2b`,
`campaign:<yyyy-mm>-<name>` (to attribute replies/bookings).

## Offer ladder (use the lowest rung that converts)
1. No offer, just relevance + open slots ("we're on your street Thursday")
2. Free add-on (screen clean, downspout flush, track/sill detail)
3. Bundle price (windows + gutters same visit)
4. Fixed $ off ($25 / $50) with a real deadline
5. Recurring plan (quarterly/bi-annual) with a per-visit discount
Referral: **$25 off for both** the referrer and the new customer (pending owner approval).

## Seasonal calendar (Placer County)
| Month | Lead message | Segment focus |
|---|---|---|
| Nov to Dec | Gutters before the big storms; holiday lights install | everyone, lapsed |
| Jan | Storm aftermath: overflowing gutters, dirty windows after rain | gutters, windows |
| Feb to Mar | Spring-ready windows; book early, calendar fills | past window customers |
| Apr to May | Pollen on solar = lost output; house wash | solar owners, homeowners |
| Jun to Aug | Peak solar season; driveway/patio before BBQs and parties | solar, pressure wash |
| Sep to Oct | Fall gutter pre-book; holiday lights reservations | everyone, recurring upsell |

## Channel rules
- **SMS** (our main channel, most customers only have a phone on file):
  blasts ≤ 160 chars, send Tue to Thu 10 AM to 1 PM or 4:30 to 6:30 PM.
  1 blast + max 1 follow-up per campaign, 2+ weeks between campaigns to the
  same person. Credits: check `flyra_get_sms_credits` first.
- **Email**: only 8 of 143 customers have an email today. Priority #1 is
  collecting emails (ask at booking, on estimates, in the Job Complete text).
  Connect a custom sending domain (`contact@flaircleaningcompany.com`) so
  emails stop coming from `@on.flyra.io` and land in the inbox.
- **Cold B2B**: email + phone, never cold SMS. See `cold-outreach.md`.

## Ops fixes that directly raise conversion
- Mark jobs **Completed** in Flyra the same day (many past jobs still show
  "scheduled"; post-job drips, review asks and revenue reports never fire).
- Tag every lead with a **lead source** (12 of 15 recent leads are "Untagged").
- Set the Google **review link** in org settings (currently empty) so review
  asks go to `https://g.page/r/CT7yfKy3tK5_EBI/review` automatically.
- Answer campaign replies within 5 minutes (turn on "MKT · Campaign Reply Alert").
