# Flair Cleaning Co — Commission Tracker

This is a **payables ledger, not a schedule**: it only contains jobs that
have actually been completed, so it always shows exactly what's owed to
each salesman, technician, and owner. Scheduled/upcoming jobs are not
added until they're done.

**Sheet:** https://docs.google.com/spreadsheets/d/1XuqFEKQ3CcaifvcHo-UAQSmGJjsJLBXG4EjOnsFz5ws/edit

> Note: until the Google Sheets connection is authenticated (cell-level
> edits), each update recreates the file and this link changes. Check here
> for the current link if an old one stops working.

## What it tracks

One row per completed job (deal), grouped by day (the date is only shown
on the first job of each day; later jobs that day just show the time):

- Customer first/last name, phone, address
- Time of the job
- Price
- Salesman and technician who worked the job
- Computed commission split

## Commission formula

- **Salesman:** 40% of the job price, always.
- **Technician:** 30%, 32.5%, or 35% of the price, set per job depending on
  which technician did the work (Flyra doesn't track this rate itself, so
  it's entered directly in the sheet's "Tech Rate" column).
- **Company:** whatever's left after the above two cuts — split 50/50
  between Santana and Will.

This always sums to 100% of the job price, whatever technician rate applies.

## Keeping it up to date

Jobs are added by telling Claude which jobs got completed (customer, price,
day/time) — Claude cross-references Flyra for the customer/job details and
appends the row. Nothing is added automatically from Flyra's schedule; a
job only lands here once it's actually done.
