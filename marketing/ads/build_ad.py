import sys
groups = {
 "Holiday Lights": {
  "headlines": ["Holiday Light Installation","Christmas Lights Installed","Granite Bay Holiday Lights","Roseville Light Installers","We Hang Them, We Take Down","Install + January Takedown","Book Before Dec 10","Local & Owner-Run Crew","Free Quote Today","No Ladders For You","Rooflines, Trees & More","Call Flair Cleaning Co","5-Star Rated Local Crew","Folsom & El Dorado Hills"],
  "descriptions": ["Professional holiday light install and January takedown. Local Granite Bay crew. Call now.","Skip the ladder this year. We hang your lights and take them down after the holidays.","Spots fill fast before mid-December. Call for a free quote and pick your install day.","Rooflines, trees and walkways. Owner-run and 5-star rated by local homeowners."],
  "keywords": ['[christmas light installation]','"christmas light installers near me"','"holiday light installation"','"christmas lights installation granite bay"','"christmas light installation roseville"','"christmas light installation folsom"','"holiday lighting company"','[christmas light hanging service]'],
 },
 "Gutter Cleaning": {
  "headlines": ["Gutter Cleaning Granite Bay","Gutter Cleaning Roseville","Gutters Cleared Before Rain","Every Downspout Flushed","Photos After Every Job","Local & Owner-Run Crew","Free Quote Today","Call Flair Cleaning Co","5-Star Rated Local Crew","Folsom, Rocklin & Loomis","Book This Week","Stop Gutter Overflow"],
  "descriptions": ["Gutters cleared and every downspout flushed before the next storm. Call for a quote.","Local Granite Bay crew. We send before and after photos so you know it was done right.","Overflowing gutters damage fascia and foundations. Book a cleaning this week.","Add windows or a driveway wash to the same visit. Owner-run and 5-star rated by neighbors."],
  "keywords": ['"gutter cleaning near me"','[gutter cleaning service]','"gutter cleaning granite bay"','"gutter cleaning roseville"','"gutter cleaning folsom"','"gutter cleaning rocklin"','"gutter cleaning el dorado hills"','"downspout cleaning"'],
 },
}
ok=True
for g,d in groups.items():
    for h in d["headlines"]:
        if len(h)>30: print("HEADLINE TOO LONG",g,len(h),h); ok=False
    for x in d["descriptions"]:
        if len(x)>90: print("DESC TOO LONG",g,len(x),x); ok=False
    if not 3<=len(d["headlines"])<=15: ok=False
print("ALL WITHIN LIMITS" if ok else "FIX NEEDED")
if "--md" in sys.argv:
    out=[]
    for g,d in groups.items():
        out.append(f"### Ad group: {g}\n\n**Keywords** (paste as-is; brackets = exact, quotes = phrase)\n```\n"+"\n".join(d["keywords"])+"\n```\n")
        out.append("**Headlines** (each ≤ 30 characters)\n```\n"+"\n".join(d["headlines"])+"\n```\n")
        out.append("**Descriptions** (each ≤ 90 characters)\n```\n"+"\n".join(d["descriptions"])+"\n```\n")
    open("adgroups.md","w").write("\n".join(out))
