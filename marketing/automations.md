# Flyra automations built for marketing

All created **switched OFF** on 2026-11-19. Turn on only after owner approval
(`flyra_enable_automation`). Quiet hours 7:30 PM to 8:30 AM on all text drips.

| Name | Flyra id | Trigger | Touches | Status |
|---|---|---|---|---|
| MKT · New Lead Nurture (5-touch) | `dec9b15c-5a8f-4d9b-989d-0b72e27ade53` | lead.created | SMS now → email d1 → SMS d3 → email d7 → SMS d14 (breakup) | OFF |
| MKT · Post-Job Referral → Cross-sell → Rebook | `333d4aa7-143e-4da7-a87d-1d5408811545` | job.completed | SMS+email d4 referral → email d49 cross-sell → SMS+email d154 rebook | OFF |
| MKT · Win-back (not serviced 180+ days) | `1c822217-6244-47d2-bb88-d193bac52d4d` | weekly Tue 10:15, 25 customers per batch | SMS+email → SMS d4 (free add-on) | OFF |
| MKT · Quoted, Not Booked (rescue) | `2addbeb8-4124-4b94-aca3-11249b9797c3` | lead idle 72h in "Quoted No Cleaning" | SMS+email → SMS d5 → move to "No Response" d15 | OFF |
| MKT · Campaign Reply Alert | `f7320317-1b18-4de0-9c3c-46ede9a981f3` | sms_blast.replied | notifies admins | **ON** (2026-11-19) |

All stop when the person replies (except the alert). Edit copy in Flyra or
ask Claude; keep this table in sync.

## Notes / before enabling
- Win-back also reaches **never-serviced** customers (43 have 0 jobs), which is
  intended. First run would hit up to 25 people; preview with
  `flyra_preview_automation_run` before turning on.
- Post-job drip relies on jobs being marked **Completed**.
- Referral text promises **$25 off for both**; confirm the owners want that offer.
- Lead nurture overlaps with Flyra's "Welcome Email" only after a first booking, so no double-up.
- Existing built-ins (estimate follow-ups, review follow-ups, reminders) left untouched.
