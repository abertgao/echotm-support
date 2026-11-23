from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.lang=None; self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="html": self.lang=a.get("lang")
        if tag=="h1":self.h1+=1
        if "id" in a:self.ids.add(a["id"])
        for key in ["href","src"]:
            if key in a:self.links.append(a[key])
errors=[]; count=0
for f in ROOT.rglob("*.html"):
    if ".git" in f.parts:continue
    count+=1;p=Page();p.feed(f.read_text())
    if not p.lang or p.h1!=1:errors.append(str(f.relative_to(ROOT))+": missing language or single heading")
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        if not u.path:
            if u.fragment and u.fragment not in p.ids:errors.append(str(f)+": missing anchor "+link)
            continue
        target=ROOT/unquote(u.path).lstrip("/") if u.path.startswith("/") else f.parent/unquote(u.path)
        if target.is_dir():target=target/"index.html"
        if not target.exists():errors.append(str(f.relative_to(ROOT))+": broken "+link)
if (ROOT/"CNAME").read_text().strip()!="echo.tendazl.com":errors.append("wrong custom domain")
if errors:print("\n".join(errors));sys.exit(1)
print(f"Checked {count} HTML pages: local links, assets, anchors, heading, language and custom domain OK.")
