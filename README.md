# Flair Cleaning Co — Commission Tracker

We track every job's commission split in a Google Sheet, synced from Flyra
(our CRM/scheduling system) on request rather than as standalone app code.

**Sheet:** https://docs.google.com/spreadsheets/d/1AWCvXBNPqZ2gIZkdvKqPEDw2JFW6t8n0NtPDwpsP8Ws/edit

## What it tracks

One row per job (deal), grouped by day (the date is only shown on the first
job of each day; later jobs that day just show the time):

- Customer first/last name, phone, address
- Time of the job and its status
- Price
- Salesman and technician assigned to the job
- Computed commission split

## Commission formula

- **Salesman:** 40% of the job price, always.
- **Technician:** 30%, 32.5%, or 35% of the price, set per job depending on
  which technician did the work (Flyra doesn't track this rate itself, so
  it's entered directly in the sheet's "Tech Rate" column).
- **Company:** whatever's left after the above two cuts — split 50/50
  between Santana and Will.

This always sums to 100% of the job price, whatever technician rate applies.
Cancelled jobs are listed for visibility but excluded from commission
totals.

## Keeping it up to date

The sheet is not live-synced. When new jobs need to be pulled in from Flyra,
ask Claude to refresh it — it re-reads the current sheet, adds new/changed
jobs from Flyra by matching on the "Flyra Job ID" column, and leaves any
technician/rate you've already filled in untouched.
