# Cold outreach (B2B)

> **Updated rules:** `outbound/cold-email-system.md` wins over this file:
> 3 emails max (first + 2 value follow-ups), one angle per test, manual sends first.
> The 4-touch sequences below are kept for reference; drop E3/E4, or switch them to a walk-in or call.

Channel: **email + phone only** (no cold SMS; TCPA). Track prospects in a
Flyra pipeline "B2B Outreach" (to create on approval) with stages:
`Researched → Contacted → Replied → Walkthrough/Quote → Won → Lost/Not now`.
Log each prospect as a lead with source "Cold outreach" and tag `b2b`.

## Target list (highest value first)
| Segment | Why they buy | Offer | Where to find them |
|---|---|---|---|
| **Property managers / HOAs** (Roseville, Rocklin, Granite Bay, Folsom) | dozens of units, recurring gutters & windows, board wants a reliable vendor | Free walkthrough + per-building recurring price | CAI chapter directory, Google Maps "HOA management", HOA sites |
| **Storefront retail & restaurants** (Galleria area, Fountains, Palladio, Old Folsom) | dirty glass = lost customers | Monthly/bi-weekly storefront glass route | walk the plazas, Google Maps |
| **Realtors** | listing prep and move-out, need it fast | "Listing-ready" windows + pressure wash package, 72h turnaround | brokerage rosters, open houses |
| **Solar installers & roofers** | customers ask "who cleans panels?" | referral partnership, $X per referred job | installer sites, Google Maps |
| **Small offices / medical / dental** | first impression, insurance-friendly vendor | quarterly exterior windows | Google Maps, chamber of commerce |
| **Churches, schools, gyms** | big glass, tight budgets, recurring | bi-annual plan | directories |

## Email sequence: Property managers / HOAs (4 touches over 14 days)
**E1 (day 0)** Subject: `Gutters & windows for {community}`
> Hi {first_name}, I'm with Flair Cleaning Co, based in Granite Bay. We handle
> gutters, windows, solar and pressure washing for homes and communities
> around Placer County. Before the storms hit, most boards want gutters
> cleared on a schedule so they're not fielding overflow complaints.
> Would a free walkthrough of {community} and a per-building price be useful?
> Takes 20 minutes, no obligation.
> (signature + address + "reply 'no thanks' and I won't follow up")

**E2 (day 3)** Subject: `re: Gutters & windows for {community}`
> Quick follow-up. One idea: we can quote a single building first so you can
> see the work before committing to the whole property. Worth a look?

**Call (day 6)**: "Hi, this is ___ with Flair Cleaning, I sent a note about
gutter and window service for {community}. Who handles exterior maintenance
vendors there?" Goal: get the decision-maker + book walkthrough.

**E3 (day 10)** Subject: `Before/after from a Granite Bay property`
> Attach one before/after photo. "Here's a recent one near you. Happy to do
> the same for {community}. Thursday or Friday for a quick walkthrough?"

**E4 (day 14) breakup** Subject: `Should I close your file?`
> I haven't heard back, so I'll assume timing isn't right. If gutters or
> windows come up at {community}, just reply and I'll get you a price same day.

## Email sequence: Storefronts (walk-in + 3 emails)
1. **Walk in** with a card, ask for the owner/manager; offer to do the front
   glass free once ("see if you like it"). Log as lead.
2. E1 (day 1): "Great meeting you, here's the price for a recurring
   every-2-weeks route: $__. Includes doors and frames."
3. E2 (day 5): photo of their clean glass if we did the free one.
4. E3 (day 12): "Want to lock in your spot on the route? We service the
   plaza on ___s."

## Realtor partnership email
Subject: `Listing-ready in 72 hours`
> Hi {first_name}, Flair Cleaning Co here. We help agents around Granite Bay
> and Roseville get listings photo-ready fast: windows inside & out, driveway
> pressure wash, gutters. Flat package pricing, 72-hour turnaround, and your
> sellers don't need to be home. Want our listing-prep price sheet?

## Tracking
Per sequence, weekly: prospects added, emails sent, reply rate, walkthroughs
booked, quotes sent, won $, cost (time). Log in `campaign-log.csv` with
channel `email-b2b` / `call-b2b`.
