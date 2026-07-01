from html.parser import HTMLParser
from pathlib import Path
import sys, urllib.parse
BASE = "/digital-governance-observatory"
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        for k,v in attrs:
            if k in {"href","src"} and v:
                self.links.append(v)
errors=[]
for f in Path('.').rglob('*.html'):
    if '.git' in f.parts: continue
    p=Parser(); p.feed(f.read_text(encoding='utf-8'))
    for link in p.links:
        if link.startswith(('http://','https://','mailto:','#','data:')): continue
        path=urllib.parse.urlparse(link).path
        if not path.startswith(BASE):
            errors.append(f'{f}: not under base path: {link}'); continue
        local=path[len(BASE):] or '/'
        target=Path('.')/(local.strip('/') or 'index.html')
        if local.endswith('/'):
            target=Path('.')/local.strip('/')/'index.html'
        if not target.exists():
            errors.append(f'{f}: broken {link} -> {target}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: all internal links resolve and use /digital-governance-observatory/ base path')
