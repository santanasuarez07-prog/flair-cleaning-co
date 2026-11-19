import sys; sys.path.insert(0,'.')
from prospects import P
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter as L

F="Arial"; HDR=PatternFill("solid",fgColor="1F3A5F"); HF=Font(name=F,bold=True,color="FFFFFF")
INP=PatternFill("solid",fgColor="FFF4CC"); SUB=PatternFill("solid",fgColor="E8EEF5")
base=Font(name=F,size=10); bold=Font(name=F,size=10,bold=True)
N=1000  # rows prepared for growth
wb=Workbook()
dash=wb.active; dash.title="Dashboard"
pr=wb.create_sheet("Prospects"); lg=wb.create_sheet("Outreach Log"); ls=wb.create_sheet("Lists")

STATUSES=[("New","No","No","No"),("Drafted","No","No","No"),("Contacted","Yes","No","Yes"),("Follow-up 1 sent","Yes","No","Yes"),("Follow-up 2 sent","Yes","No","Yes"),("Replied","Yes","Yes","Yes"),("Meeting / quote","Yes","Yes","Yes"),("Won","Yes","Yes","No"),("Not now","Yes","Yes","No"),("Lost / no thanks","Yes","Yes","No")]
SEGS=[("Shopping center",600),("HOA / property mgmt",500),("Commercial property mgmt",500),("Golf / club",400),("Real estate office",300),("Business association",300),("Solar installer (partner)",200),("Church / school",150),("Restaurant / cafe",100),("Dental / medical",80),("Retail / shop",80)]
CITIES=["Granite Bay","Roseville","Rocklin","Loomis","Folsom","El Dorado Hills","Auburn","Lincoln"]
CHANNELS=["Email","Call","Walk-in","Instagram / social","Text (only if they texted us first)"]
OUTCOMES=["Sent","Replied - interested","Replied - not now","Replied - no thanks","Meeting booked","Won","Bounced","No answer","Talked in person"]
VARIANTS=["B1 Founding 5","B3 Storm Season","B2 Audition","B4 Three-Liner","B5 Photo Proof","B6 Question CTA","Walk-in script","Call script"]
PRIOS=["A","B","C"]

# ---------- Lists ----------
ls["A1"]="Status"; ls["B1"]="Counts as contacted"; ls["C1"]="Counts as a reply"; ls["D1"]="Open pipeline"
for i,(s,c,r,o) in enumerate(STATUSES,2): ls.cell(i,1,s); ls.cell(i,2,c); ls.cell(i,3,r); ls.cell(i,4,o)
ls["F1"]="Segment"; ls["G1"]="Est. monthly value ($), your estimate"
for i,(s,v) in enumerate(SEGS,2):
    ls.cell(i,6,s); c=ls.cell(i,7,v); c.fill=INP; c.number_format='$#,##0'
ls.cell(len(SEGS)+3,6,"Yellow cells are inputs. These values are placeholder estimates of monthly revenue per account; replace them with your real prices.").font=Font(name=F,size=9,italic=True)
ls["I1"]="City"; ls["J1"]="Channel"; ls["K1"]="Outcome"; ls["L1"]="Variant"; ls["M1"]="Priority"
for col,vals in ((9,CITIES),(10,CHANNELS),(11,OUTCOMES),(12,VARIANTS),(13,PRIOS)):
    for i,v in enumerate(vals,2): ls.cell(i,col,v)
for c in ls[1]: c.font=HF; c.fill=HDR
for col,w in zip("ABCDEFGHIJKLM",[18,20,16,14,3,26,22,3,16,30,22,18,9]): ls.column_dimensions[col].width=w

# ---------- Prospects ----------
H=["ID","Business","Segment","City","Address","Phone","Email","Website","Contact name","Priority","Status","Variant used","Last touch","Next step","Next step date","Est. monthly value","Won monthly value","Touches logged","Notes","Source"]
for j,h in enumerate(H,1):
    c=pr.cell(1,j,h); c.font=HF; c.fill=HDR; c.alignment=Alignment(wrap_text=True,vertical="center")
nseg=len(SEGS)+1
for i,p in enumerate(P,2):
    vals=[i-1,p["business"],p["segment"],p["city"],p["address"],p["phone"],"","",p["contact"],p["priority"],p["status"],
          ("B1 Founding 5" if p["status"]=="Drafted" else ""),None,
          ("Add email address, then send draft" if p["status"]=="Drafted" else ""),None]
    for j,v in enumerate(vals,1):
        if v is not None: pr.cell(i,j,v)
    pr.cell(i,19,p["notes"]); pr.cell(i,20,p["source"])
# B3 drafts
for i,p in enumerate(P,2):
    if p["business"] in ("Dr. Colby Smith, DDS","Make A Smile Dental / S. Jang DDS","Granite Bay Real Estate, Inc.","Riverside Management & Financial Services","Quarry Ponds Town Center (property manager)"):
        pr.cell(i,12,"B3 Storm Season")
for r in range(2,N+2):
    pr.cell(r,16,f'=IF($B{r}="","",IFERROR(VLOOKUP($C{r},Lists!$F$2:$G${nseg},2,FALSE),0))').number_format='$#,##0'
    pr.cell(r,17).number_format='$#,##0'; pr.cell(r,17).fill=INP
    pr.cell(r,18,f'=IF($B{r}="","",COUNTIF(\'Outreach Log\'!$B$2:$B${N+1},$A{r}))')
    pr.cell(r,13).number_format='yyyy-mm-dd'; pr.cell(r,15).number_format='yyyy-mm-dd'
for row in pr.iter_rows(min_row=2,max_row=N+1):
    for c in row:
        if c.font.name!=F: c.font=base
widths=[5,40,22,14,32,15,26,22,18,8,17,17,11,30,12,11,11,9,30,24]
for j,w in enumerate(widths,1): pr.column_dimensions[L(j)].width=w
pr.freeze_panes="C2"; pr.auto_filter.ref=f"A1:T{N+1}"
def dv(ws,rng,src):
    d=DataValidation(type="list",formula1=src,allow_blank=True); ws.add_data_validation(d); d.add(rng)
dv(pr,f"C2:C{N+1}",f"=Lists!$F$2:$F${nseg}")
dv(pr,f"D2:D{N+1}",f"=Lists!$I$2:$I${len(CITIES)+1}")
dv(pr,f"J2:J{N+1}",f"=Lists!$M$2:$M${len(PRIOS)+1}")
dv(pr,f"K2:K{N+1}",f"=Lists!$A$2:$A${len(STATUSES)+1}")
dv(pr,f"L2:L{N+1}",f"=Lists!$L$2:$L${len(VARIANTS)+1}")
red=PatternFill("solid",fgColor="F8D7DA")
pr.conditional_formatting.add(f"O2:O{N+1}",FormulaRule(formula=[f'AND($O2<>"",$O2<TODAY(),$K2<>"Won",$K2<>"Lost / no thanks")'],fill=red))
grn=PatternFill("solid",fgColor="D4EDDA")
pr.conditional_formatting.add(f"A2:T{N+1}",FormulaRule(formula=['$K2="Won"'],fill=grn))

# ---------- Outreach Log ----------
LH=["Date","Prospect ID","Business","City","Channel","Variant","Touch # (1 = first email, 2-3 = follow-ups)","Subject / what was said","Outcome","Notes"]
for j,h in enumerate(LH,1):
    c=lg.cell(1,j,h); c.font=HF; c.fill=HDR; c.alignment=Alignment(wrap_text=True,vertical="center")
for r in range(2,N+2):
    lg.cell(r,1).number_format='yyyy-mm-dd'
    lg.cell(r,3,f'=IF($B{r}="","",IFERROR(INDEX(Prospects!$B$2:$B${N+1},MATCH($B{r},Prospects!$A$2:$A${N+1},0)),"ID not found"))')
    lg.cell(r,4,f'=IF($B{r}="","",IFERROR(INDEX(Prospects!$D$2:$D${N+1},MATCH($B{r},Prospects!$A$2:$A${N+1},0)),""))')
    for c in lg[r]: c.font=base
for j,w in enumerate([11,10,36,14,16,18,14,40,22,30],1): lg.column_dimensions[L(j)].width=w
lg.freeze_panes="A2"
dv(lg,f"E2:E{N+1}",f"=Lists!$J$2:$J${len(CHANNELS)+1}")
dv(lg,f"F2:F{N+1}",f"=Lists!$L$2:$L${len(VARIANTS)+1}")
dv(lg,f"I2:I{N+1}",f"=Lists!$K$2:$K${len(OUTCOMES)+1}")
d=DataValidation(type="whole",operator="between",formula1="1",formula2="3",allow_blank=True); lg.add_data_validation(d); d.add(f"G2:G{N+1}")

# ---------- Dashboard ----------
PS="Prospects"; R=f"$2:$"; 
st=f"{PS}!$K$2:$K${N+1}"; ct=f"{PS}!$D$2:$D${N+1}"; sg=f"{PS}!$C$2:$C${N+1}"; nm=f"{PS}!$B$2:$B${N+1}"
ev=f"{PS}!$P$2:$P${N+1}"; wv=f"{PS}!$Q$2:$Q${N+1}"
LG="'Outreach Log'"; ldate=f"{LG}!$A$2:$A${N+1}"; lch=f"{LG}!$E$2:$E${N+1}"; lvar=f"{LG}!$F$2:$F${N+1}"; ltouch=f"{LG}!$G$2:$G${N+1}"; lout=f"{LG}!$I$2:$I${N+1}"; lid=f"{LG}!$B$2:$B${N+1}"
dash["A1"]="Flair Cleaning Co: Outbound CRM dashboard"; dash["A1"].font=Font(name=F,size=16,bold=True,color="1F3A5F")
dash["A2"]='=CONCATENATE("Updated live from the Prospects and Outreach Log tabs. Today: ",TEXT(TODAY(),"mmm d, yyyy"))'; dash["A2"].font=Font(name=F,size=9,italic=True)
def hdr(r,c,labels):
    for j,t in enumerate(labels):
        x=dash.cell(r,c+j,t); x.font=HF; x.fill=HDR; x.alignment=Alignment(wrap_text=True,vertical="center")
# status table (helper for KPIs)
hdr(4,6,["Status","Prospects","Counts as contacted","Counts as a reply","Open pipeline"])
s0=5
for i,(s,_,_,_) in enumerate(STATUSES):
    r=s0+i
    dash.cell(r,6,f"=Lists!A{i+2}"); dash.cell(r,7,f"=COUNTIF({st},F{r})")
    dash.cell(r,8,f"=Lists!B{i+2}"); dash.cell(r,9,f"=Lists!C{i+2}"); dash.cell(r,10,f"=Lists!D{i+2}")
s1=s0+len(STATUSES)-1
SR=f"$G${s0}:$G${s1}"
# KPIs
hdr(4,1,["Key numbers","Value"])
k=[("Prospects in list",f"=COUNTA({nm})",'0'),
   ("Contacted",f'=SUMIFS({SR},$H${s0}:$H${s1},"Yes")','0'),
   ("Replied (any reply)",f'=SUMIFS({SR},$I${s0}:$I${s1},"Yes")','0'),
   ("Reply rate",None,'0.0%'),
   ("Meetings / quotes",f'=COUNTIF({st},"Meeting / quote")','0'),
   ("Won accounts",f'=COUNTIF({st},"Won")','0'),
   ("Win rate (won ÷ contacted)",None,'0.0%'),
   ("Won monthly revenue",f"=SUM({wv})",'$#,##0'),
   ("Open pipeline, est. monthly",f'=SUMPRODUCT(SUMIFS({ev},{st},$F${s0}:$F${s1})*($J${s0}:$J${s1}="Yes"))','$#,##0'),
   ("Untouched prospects (New)",f'=COUNTIF({st},"New")','0'),
   ("Follow-ups overdue",f'=COUNTIFS({PS}!$O$2:$O${N+1},"<"&TODAY(),{st},"<>Won",{st},"<>Lost / no thanks")','0'),
   ("Touches logged, total",f"=COUNTA({lid})",'0'),
   ("Touches this week (Mon-today)",f'=COUNTIFS({ldate},">="&(TODAY()-WEEKDAY(TODAY(),2)+1))','0'),
   ("Touches today",f'=COUNTIFS({ldate},TODAY())','0')]
for i,(lab,fm,nf) in enumerate(k):
    r=5+i; dash.cell(r,1,lab).font=bold
    if lab=="Reply rate": fm="=IF(B6=0,0,B7/B6)"
    if lab.startswith("Win rate"): fm="=IF(B6=0,0,B10/B6)"
    c=dash.cell(r,2,fm); c.number_format=nf; c.font=Font(name=F,size=11,bold=True)
dash.cell(5+len(k),1,"Targets: reply rate > 6%, meetings > 2% of contacted. Cold email limit: 10/day per inbox in week 1, 30-40 max later.").font=Font(name=F,size=9,italic=True)
# by city
r0=22; hdr(r0,1,["City","Prospects","Contacted","Replied","Won","Reply rate","Open pipeline, est. monthly"])
cflags=f'$H${s0}:$H${s1}'
for i,cname in enumerate(CITIES):
    r=r0+1+i; dash.cell(r,1,f"=Lists!I{i+2}")
    dash.cell(r,2,f"=COUNTIF({ct},$A{r})")
    dash.cell(r,3,f'=SUMPRODUCT(COUNTIFS({ct},$A{r},{st},$F${s0}:$F${s1})*($H${s0}:$H${s1}="Yes"))')
    dash.cell(r,4,f'=SUMPRODUCT(COUNTIFS({ct},$A{r},{st},$F${s0}:$F${s1})*($I${s0}:$I${s1}="Yes"))')
    dash.cell(r,5,f'=COUNTIFS({ct},$A{r},{st},"Won")')
    dash.cell(r,6,f"=IF(C{r}=0,0,D{r}/C{r})").number_format='0.0%'
    dash.cell(r,7,f'=SUMPRODUCT(SUMIFS({ev},{ct},$A{r},{st},$F${s0}:$F${s1})*($J${s0}:$J${s1}="Yes"))').number_format='$#,##0'
# by segment
r1=r0+len(CITIES)+3; hdr(r1,1,["Segment","Prospects","Contacted","Replied","Won","Reply rate","Est. monthly value per account"])
for i,(s,_) in enumerate(SEGS):
    r=r1+1+i; dash.cell(r,1,f"=Lists!F{i+2}")
    dash.cell(r,2,f"=COUNTIF({sg},$A{r})")
    dash.cell(r,3,f'=SUMPRODUCT(COUNTIFS({sg},$A{r},{st},$F${s0}:$F${s1})*($H${s0}:$H${s1}="Yes"))')
    dash.cell(r,4,f'=SUMPRODUCT(COUNTIFS({sg},$A{r},{st},$F${s0}:$F${s1})*($I${s0}:$I${s1}="Yes"))')
    dash.cell(r,5,f'=COUNTIFS({sg},$A{r},{st},"Won")')
    dash.cell(r,6,f"=IF(C{r}=0,0,D{r}/C{r})").number_format='0.0%'
    dash.cell(r,7,f"=Lists!G{i+2}").number_format='$#,##0'
# by variant
r2=r1+len(SEGS)+3; hdr(r2,1,["Email variant (A/B test)","First emails sent","Replies","Reply rate","Meetings + won","Booking rate","Status"])
for i,v in enumerate(VARIANTS[:6]):
    r=r2+1+i; dash.cell(r,1,f"=Lists!L{i+2}")
    dash.cell(r,2,f'=COUNTIFS({lvar},$A{r},{ltouch},1,{lch},"Email")')
    dash.cell(r,3,f'=COUNTIFS({lvar},$A{r},{lout},"Replied*")+COUNTIFS({lvar},$A{r},{lout},"Meeting booked")+COUNTIFS({lvar},$A{r},{lout},"Won")')
    dash.cell(r,4,f"=IF(B{r}=0,0,C{r}/B{r})").number_format='0.0%'
    dash.cell(r,5,f'=COUNTIFS({lvar},$A{r},{lout},"Meeting booked")+COUNTIFS({lvar},$A{r},{lout},"Won")')
    dash.cell(r,6,f"=IF(B{r}=0,0,E{r}/B{r})").number_format='0.0%'
    dash.cell(r,7,f'=IF(B{r}<25,"Need 25+ sends",IF(D{r}=MAX($D${r2+1}:$D${r2+6}),"Leading","Behind"))')
# activity by channel
r3=r2+9; hdr(r3,1,["Channel","Touches","Replies","Reply rate"])
for i,chn in enumerate(CHANNELS[:4]):
    r=r3+1+i; dash.cell(r,1,f"=Lists!J{i+2}")
    dash.cell(r,2,f"=COUNTIF({lch},$A{r})")
    dash.cell(r,3,f'=COUNTIFS({lch},$A{r},{lout},"Replied*")+COUNTIFS({lch},$A{r},{lout},"Talked in person")+COUNTIFS({lch},$A{r},{lout},"Meeting booked")+COUNTIFS({lch},$A{r},{lout},"Won")')
    dash.cell(r,4,f"=IF(B{r}=0,0,C{r}/B{r})").number_format='0.0%'
for row in dash.iter_rows(min_row=4,max_row=r3+6):
    for c in row:
        if c.font.color is None or c.font.color.rgb!="FFFFFFFF":
            if not c.font.bold: c.font=base
for col,w in zip("ABCDEFGHIJ",[30,14,12,12,10,18,14,14,14,12]): dash.column_dimensions[col].width=w
dash.freeze_panes="A4"

# ---------- How to use ----------
hw=wb.create_sheet("How to use",1)
lines=["How to use this CRM",
"",
"1. Prospects tab: one row per business. Fill in Email when you find it (from their website or Google listing; never guess).",
"2. Every time you email, call or walk in, add a row to the Outreach Log: date, Prospect ID, channel, variant, touch #, outcome.",
"3. Then update the prospect's Status, Last touch, Next step and Next step date. Overdue next steps turn red.",
"4. When an account signs, set Status to Won and type its monthly revenue in Won monthly value (yellow). The row turns green.",
"5. The Dashboard updates by itself: reply rate, wins, pipeline by city and segment, and which email variant is winning.",
"",
"Statuses: New → Drafted → Contacted → Follow-up 1 sent → Follow-up 2 sent → Replied → Meeting / quote → Won (or Not now / Lost).",
"Rules: max 3 emails per business (first + 2 follow-ups), then switch to a call or walk-in. No cold texts.",
"Yellow cells are inputs. Est. monthly value per segment lives on the Lists tab; replace the placeholder estimates with your real prices.",
"",
"Contact details come from public directories (Nov 2026) and may be out of date; call or check the website before relying on them."]
for i,t in enumerate(lines,1):
    c=hw.cell(i,1,t); c.font=Font(name=F,size=14 if i==1 else 10,bold=(i==1))
hw.column_dimensions["A"].width=130
out=sys.argv[1]; wb.save(out); print("saved",out,len(P),"prospects")
