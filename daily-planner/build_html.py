"""Generates planner.html — a one-page A4 Arabic (RTL) daily planner."""
from pathlib import Path

ICONS = {
    "book": '<path d="M12 6.2C9.8 4.7 6.9 4.2 3.5 4.6v13.6c3.4-.4 6.3.1 8.5 1.6 2.2-1.5 5.1-2 8.5-1.6V4.6c-3.4-.4-6.3.1-8.5 1.6z"/><path d="M12 6.2v13.6"/><path d="M6.2 8.6c1.3 0 2.5.2 3.5.7M6.2 11.6c1.3 0 2.5.2 3.5.7M14.3 9.3c1-.5 2.2-.7 3.5-.7M14.3 12.3c1-.5 2.2-.7 3.5-.7"/>',
    "mosque": '<path d="M2 21h20"/><path d="M8 21v-6.5h12V21"/><path d="M8.6 14.5c0-2.6 2.1-4.2 5.4-6 3.3 1.8 5.4 3.4 5.4 6"/><path d="M14 8.5V6.3"/><path d="M14.9 4.6a1.2 1.2 0 1 1-1.5-1.3 1.6 1.6 0 0 0 1.5 1.3z"/><path d="M12.4 21v-2.6a1.6 1.6 0 0 1 3.2 0V21"/><path d="M3.5 21V10.5l1-2.3 1 2.3V21"/><path d="M3.5 13h2"/>',
    "sheep": '<path d="M5.4 10.3a2 2 0 0 1 2.4-2.3 2.3 2.3 0 0 1 3.9-.6 2.3 2.3 0 0 1 3.7.4 2 2 0 0 1 2 1.3"/><path d="M5.4 10.3A2.1 2.1 0 0 0 4.6 14a2.2 2.2 0 0 0 3.3 2.3 2.3 2.3 0 0 0 3.6.3 2.3 2.3 0 0 0 3.6-.3 2.1 2.1 0 0 0 2.4-1.6"/><path d="M17.4 9.1c1.3-.7 3.6-.6 3.9 1 .3 1.7-1 3.4-2.6 3.5-.8 0-1.4-.6-1.6-1.2"/><path d="M18.2 9.2l-.9-1.6"/><path d="M7.5 16.6v3.4M10.2 17.1v2.9M13.8 17.1v2.9M16.4 16.4V20"/><circle cx="19.3" cy="10.6" r=".35" fill="currentColor"/>',
    "steth": '<path d="M5.5 3.5H4.5v5a4.5 4.5 0 0 0 9 0v-5h-1"/><path d="M9 13v2.2a5 5 0 0 0 10 0V13"/><circle cx="19" cy="10.8" r="2.2"/>',
    "school": '<path d="M2.5 21h19"/><path d="M4.5 21V11.2L12 7l7.5 4.2V21"/><path d="M12 7V2.6l3.6 1.3L12 5.2"/><path d="M10 21v-4.2h4V21"/><path d="M7.3 13.4h2M14.7 13.4h2M7.3 16.7h1.4M15.3 16.7h1.4"/><circle cx="12" cy="11.6" r="1.3"/>',
    "store": '<path d="M4.3 11v10h15.4V11"/><path d="M3 9.3 4.6 3.5h14.8L21 9.3a2.25 2.25 0 0 1-4.5.2 2.25 2.25 0 0 1-4.5 0 2.25 2.25 0 0 1-4.5 0A2.25 2.25 0 0 1 3 9.3z"/><path d="M9.6 21v-5.3h4.8V21"/><path d="M2 21h20"/>',
    "brush": '<path d="M2.3 16.6 12 12.5"/><path d="M12 12.5l9.3-3.9a1.3 1.3 0 0 1 1 2.4L13 14.9"/><path d="M13.6 11.8l-1.7-4M16.1 10.7l-1.7-4M18.6 9.7 16.9 5.7M21 8.7l-1.6-3.8"/>',
    "shower": '<path d="M5 21V7.5A4.5 4.5 0 0 1 9.5 3h0A4.5 4.5 0 0 1 14 7.5"/><path d="M9.5 11.5a4.5 4.5 0 0 1 9 0z"/><path d="M11 14.6v.4M14 14.6v.4M17 14.6v.4M12.5 17.4v.4M15.5 17.4v.4M11 20.2v.4M14 20.2v.4M17 20.2v.4"/>',
    "pencil": '<path d="M4 20l.9-4.4L15.6 4.9a2 2 0 0 1 2.9 0l.6.6a2 2 0 0 1 0 2.9L8.4 19.1z"/><path d="M13.8 6.7l3.5 3.5"/><path d="M4 20h7"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2.2"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="M7.5 13.5h2M11 13.5h2M14.5 13.5h2M7.5 17h2M11 17h2"/>',
    "chart": '<path d="M3.5 20.5h17"/><rect x="5" y="13" width="3.2" height="5.5" rx=".6"/><rect x="10.4" y="9" width="3.2" height="9.5" rx=".6"/><rect x="15.8" y="4.5" width="3.2" height="14" rx=".6"/>',
    "note": '<path d="M6 2.8h8.6l4.4 4.4v14H6z"/><path d="M14.4 2.8v4.6H19"/><path d="M9 12h7M9 15.4h7M9 18.6h4.5"/>',
    "office": '<rect x="5" y="2.8" width="14" height="18.4" rx="1.2"/><path d="M8.6 6.6h2M13.4 6.6h2M8.6 10.2h2M13.4 10.2h2M8.6 13.8h2M13.4 13.8h2"/><path d="M10.4 21.2v-3.6h3.2v3.6"/><path d="M3 21.2h18"/>',
    "person": '<circle cx="12" cy="7.8" r="4"/><path d="M4.2 21a7.8 7.8 0 0 1 15.6 0"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M2.5 12h2M19.5 12h2M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    "moon": '<path d="M19.5 14.6A8 8 0 1 1 9.4 4.5a6.4 6.4 0 0 0 10.1 10.1z"/>',
    "clock": '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.2V12l3.2 2"/>',
    "check": '<path d="M5 12.5l4.2 4.2L19 7"/>',
    "list": '<path d="M9.5 6h11M9.5 12h11M9.5 18h11"/><path d="M3.5 6l1.2 1.2L7 4.8M3.5 12l1.2 1.2L7 10.8M3.5 18l1.2 1.2L7 16.8"/>',
}


def icon(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def section_head(title, ic, extra=""):
    return (f'<div class="sh"><span class="sh-ic">{icon(ic)}</span>'
            f'<h2>{title}</h2>{extra}</div>')


def task(text, ic, tail="", cls=""):
    return (f'<div class="task {cls}"><span class="box"></span>'
            f'<span class="tic">{icon(ic)}</span><span class="tx">{text}</span>{tail}</div>')


def pill(text, ic):
    return f'<span class="pill">{icon(ic, "ic sm")}{text}</span>'


# ---------- sections ----------
prayers = ["صلاة الفجر", "صلاة الظهر", "صلاة العصر", "صلاة المغرب", "صلاة العشاء"]
religion_rows = [task("قراءة القرآن الكريم", "book", cls="quran")]
for p in prayers:
    religion_rows.append(task(
        f'{p} <span class="soft">مع الجماعة</span>', "mosque",
        tail='<span class="pbox"><span class="box s"></span></span><span class="pbox"><span class="box s"></span></span>',
        cls="prayer"))

religion = f'''
<section class="card c-rel">
  {section_head("الدين", "mosque")}
  <div class="pcols"><span></span><span class="pc">أُدِّيَت</span><span class="pc">في وقتها</span></div>
  <div class="rows">{"".join(religion_rows)}</div>
</section>'''

projects = f'''
<section class="card c-prj">
  {section_head("مشاريعي", "sheep")}
  <div class="rows">
    {task("جرد الأغنام", "sheep")}
    {task("فحص الأغنام والاطمئنان عليها", "steth")}
  </div>
</section>'''

work = f'''
<section class="card c-wrk">
  {section_head("دواماتي", "office")}
  <div class="rows">
    {task("دوام المدرسة", "school", pill("الساعة 6:00 صباحاً", "clock"))}
    {task("دوام المدرسة", "school", pill("الساعة 12:00 ظهراً", "clock"))}
    {task("دوام المحل", "store")}
  </div>
</section>'''

personal = f'''
<section class="card c-per">
  {section_head("أموري الشخصية", "person")}
  <div class="rows">
    {task("تفريش الأسنان", "brush", pill("صباحاً", "sun"))}
    {task("تفريش الأسنان", "brush", pill("مساءً", "moon"))}
    {task('الاستحمام <span class="soft">(الشاور)</span>', "shower")}
  </div>
</section>'''

side_lines = "".join(
    f'<div class="task wline"><span class="box"></span><span class="tic">{icon("pencil")}</span><span class="line"></span></div>'
    for _ in range(5))
side = f'''
<section class="card c-side">
  {section_head("مهام جانبية", "list")}
  <div class="rows">{side_lines}</div>
</section>'''

table_rows = "".join('<tr><td></td><td></td><td></td></tr>' for _ in range(8))
sheep_log = f'''
<section class="card c-log">
  {section_head("سجل جرد الأغنام اليومي", "sheep")}
  <table class="log">
    <colgroup><col style="width:44%"><col style="width:17%"><col style="width:39%"></colgroup>
    <thead><tr>
      <th>{icon("sheep", "ic sm")}اسم الشبك / نوع الأغنام</th>
      <th>العدد</th>
      <th>{icon("note", "ic sm")}ملاحظات</th>
    </tr></thead>
    <tbody>{table_rows}</tbody>
  </table>
</section>'''

segs = "".join(f'<span class="seg"><i></i><b>{n}</b></span>' for n in range(10, 101, 10))
footer = f'''
<section class="card c-foot">
  <div class="frow">
    <div class="field f-date">
      <span class="flabel"><span class="fic">{icon("calendar")}</span>التاريخ:</span>
      <span class="datebox"><span class="dl s2"></span><i>/</i><span class="dl s2"></span><i>/</i><span class="dl s4"></span></span>
    </div>
    <div class="field f-pct">
      <span class="flabel"><span class="fic">{icon("chart")}</span>نسبة إنجاز المهام:</span>
      <span class="dl s3"></span><span class="pct">%</span>
      <span class="segs">{segs}</span>
    </div>
  </div>
  <div class="field f-notes">
    <span class="flabel"><span class="fic">{icon("note")}</span>ملاحظات اليوم:</span>
    <div class="nlines"><span class="line"></span><span class="line"></span></div>
  </div>
</section>'''

days = ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"]
days_html = "".join(f'<span class="day">{d}</span>' for d in days)
header = f'''
<header class="top">
  <div class="brand">
    <div class="logo">{icon("check")}</div>
    <div>
      <h1>خطتي اليومية</h1>
      <p>الدين · المشاريع · الدوامات · الأمور الشخصية</p>
    </div>
  </div>
  <div class="days">{days_html}</div>
</header>'''

css = Path(__file__).with_name("planner.css").read_text(encoding="utf-8")

html = f'''<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>خطتي اليومية</title>
<style>{css}</style>
</head>
<body>
<main class="page">
  {header}
  <div class="grid g1">
    {religion}
    <div class="stack">{projects}{work}</div>
  </div>
  <div class="grid g2">
    {personal}
    {side}
  </div>
  {sheep_log}
  {footer}
</main>
</body>
</html>'''

Path(__file__).with_name("planner.html").write_text(html, encoding="utf-8")
print("planner.html written")
