from pathlib import Path
from html.parser import HTMLParser
import sys, subprocess
BASE='/digital-governance-observatory'
projects=['agentconsent','machineconsent','gulfcompute','gulfauth','gulfkyc']
articles=['human-consent-records','revocable-authorization','human-oversight-autonomous-machines','safe-revocation-emergency-stop','mapping-gulf-ai-compute','energy-cooling-sovereign-compute','passkeys-passwordless-gulf','identity-federation-regional-services','kyc-kyb-aml-overview','privacy-preserving-onboarding']
required=['README.md','LICENSE','CITATION.cff','CHANGELOG.md','AUTHORS.md','SOURCES.md','BRAND_SCREENING_NOTES.md','PROJECT_HISTORY.md','PUBLICATION_MANIFEST_SHA256.json','robots.txt','sitemap.xml','.well-known/security.txt','.github/workflows/pages.yml']
checks=[]
def add(name, ok, detail=''):
    checks.append((name, ok, detail))
add('GitHub Pages workflow exists', Path('.github/workflows/pages.yml').exists())
add('Base path present in home page', BASE in Path('index.html').read_text(encoding='utf-8'))
add('English pages exist', all(Path(p,'index.html').exists() for p in ['about','projects','research','sources','history','contact','privacy','terms','disclaimer']))
add('Arabic RTL pages exist', all(Path('ar',p,'index.html').exists() for p in ['about','projects','research','sources','history','contact','privacy','terms','disclaimer']) and 'dir="rtl"' in Path('ar/index.html').read_text(encoding='utf-8'))
add('English LTR home exists', 'dir="ltr"' in Path('index.html').read_text(encoding='utf-8'))
add('Five project pages exist in both languages', all(Path('projects',p,'index.html').exists() and Path('ar/projects',p,'index.html').exists() for p in projects))
add('At least ten article pages exist in both languages', all(Path('research',a,'index.html').exists() and Path('ar/research',a,'index.html').exists() for a in articles))
add('Required repository files exist', all(Path(f).exists() for f in required))
add('security.txt exists', Path('.well-known/security.txt').exists())
for cmd,name in [(['python3','scripts/check_links.py'],'Internal links and base path'),(['python3','scripts/check_content.py'],'Content policy')]:
    r=subprocess.run(cmd, text=True, capture_output=True)
    add(name, r.returncode==0, (r.stdout+r.stderr).strip())
for name, ok, detail in checks:
    print(('PASS' if ok else 'FAIL') + ': ' + name + (f' — {detail}' if detail else ''))
if not all(ok for _,ok,_ in checks):
    sys.exit(1)
