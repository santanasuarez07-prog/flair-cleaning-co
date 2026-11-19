# Outbound CRM

**Live Google Sheet:** https://docs.google.com/spreadsheets/d/1zwJgMdImGhk7FKVPZlMYshPuRLEniohEZKhemA9G1ww/edit
(owned by contact@flaircleaningcompany.com). This is the working copy; edit it there.

Tabs: Dashboard · How to use · Prospects (166 businesses, room for 1,000) · Outreach Log · Lists (dropdowns + segment value estimates).

- `prospects.py`: source list of researched businesses (Nov 2026, public directories)
- `build_crm.py`: rebuilds the workbook: `python3 build_crm.py out.xlsx`
- `flair-outbound-crm.xlsx`: the original upload (a snapshot; the Google Sheet is the live copy)

To add businesses in bulk, append to `prospects.py` and paste new rows into the Sheet's
Prospects tab (don't rebuild over the live Sheet, or you'll lose its logged activity).
