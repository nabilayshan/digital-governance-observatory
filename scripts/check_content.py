from pathlib import Path
import re, sys
bad=[]
for p in Path('.').rglob('*'):
    if '.git' in p.parts or not p.is_file(): continue
    if p.suffix.lower() in {'.html','.md','.xml','.txt','.json','.cff','.yml'} or p.name in {'LICENSE','_headers'}:
        s=p.read_text(encoding='utf-8', errors='ignore')
        for term in ['Lorem Ipsum','lorem ipsum','TODO','®','official Gulf authority','Government-approved','Registered trademark','Accredited','Leading company']:
            if term in s:
                bad.append(f'{p}: prohibited term {term}')
if bad:
    print('\n'.join(bad)); sys.exit(1)
print('PASS: no placeholder text, prohibited claims, or trademark symbol found')
