#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; MANIFEST=ROOT/'release'/'PUBLIC_MANIFEST.json'
ALLOWED={'.md','.json','.jsonl','.py','.yml','.yaml'}
PRIVATE=[re.compile(r'docs\.google\.com',re.I),re.compile(r'drive\.google\.com',re.I),re.compile('LIVING_LOOM_START'+'_HERE_CURRENT',re.I),re.compile(r'BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY',re.I)]
LINK=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
REQ={
'SOURCES.jsonl':{'id':str,'label':str,'author_role':str,'source_kind':str,'date_text':str,'date_status':str,'channel_completeness':str,'locator_status':str,'public_url':(str,type(None)),'access_status':str,'human_index_anchor':str,'review_state':str},
'ENTITIES.jsonl':{'id':str,'label':str,'entity_kind':str,'origin':str,'definition':str,'limits':list},
'CLAIMS.jsonl':{'id':str,'label':str,'text':str,'origin':str,'claim_kind':str,'status':str,'source_refs':list,'relation_refs':list,'rivals_or_limits':list,'revision':int,'review_state':str},
'RELATIONS.jsonl':{'id':str,'from':(str,list),'to':(str,list),'type':str,'basis':str,'conditions':list,'limits':list,'origin':str,'review_state':str},}
def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for c in iter(lambda:f.read(65536),b''): h.update(c)
 return h.hexdigest()
def files(): return sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and p!=MANIFEST and '__pycache__' not in p.parts)
def slug(s):
 s=re.sub(r'<[^>]+>','',s).lower().strip(); s=re.sub(r'[^\w\- ]','',s); return re.sub(r'\s+','-',s)
def anchors(p):
 out=set(); seen={}
 for line in p.read_text(encoding='utf-8').splitlines():
  if line.startswith('#'):
   a=slug(line.lstrip('#').strip()); n=seen.get(a,0); seen[a]=n+1; out.add(a if n==0 else f'{a}-{n}')
 return out
def main():
 e=[]; recs={}; ids={}
 for p in files():
  rel=p.relative_to(ROOT)
  if p.suffix.lower() not in ALLOWED: e.append(f'disallowed extension: {rel}')
  if '..' in rel.parts: e.append(f'path traversal: {rel}')
  if p.suffix.lower() in ALLOWED:
   text=p.read_text(encoding='utf-8')
   for q in PRIVATE:
    if q.search(text): e.append(f'private-boundary pattern in {rel}: {q.pattern}')
   if p.suffix.lower()=='.md':
    for target in LINK.findall(text):
     if target.startswith(('http://','https://','mailto:')): continue
     fp,_,frag=target.partition('#'); dest=(p.parent/fp).resolve() if fp else p.resolve()
     try: dest.relative_to(ROOT.resolve())
     except ValueError: e.append(f'link escapes root in {rel}: {target}'); continue
     if not dest.exists(): e.append(f'broken link in {rel}: {target}'); continue
     if frag and dest.suffix.lower()=='.md' and frag not in anchors(dest): e.append(f'broken fragment in {rel}: {target}')
 for name,schema in REQ.items():
  p=ROOT/'research'/name; arr=[]
  if not p.exists(): e.append(f'missing research/{name}'); continue
  for n,line in enumerate(p.read_text().splitlines(),1):
   if not line.strip(): continue
   try:o=json.loads(line)
   except Exception as x:e.append(f'invalid JSONL {name}:{n}: {x}');continue
   for k,tp in schema.items():
    if k not in o:e.append(f'missing {k} {name}:{n}')
    elif not isinstance(o[k],tp):e.append(f'invalid type {k} {name}:{n}')
   arr.append(o)
  recs[name]=arr
  seen=set()
  for o in arr:
   if 'id' not in o: continue
   if o['id'] in seen:e.append(f'duplicate id in {name}: {o["id"]}')
   seen.add(o['id'])
  ids[name]=seen
 all_global={}
 for name,s in ids.items():
  for x in s:
   if x in all_global:e.append(f'duplicate public id across {all_global[x]} and {name}: {x}')
   all_global[x]=name
 for c in recs.get('CLAIMS.jsonl',[]):
  for s in c.get('source_refs',[]):
   if s not in ids.get('SOURCES.jsonl',set()):e.append(f'claim {c.get("id")} missing source {s}')
  for r in c.get('relation_refs',[]):
   if r not in ids.get('RELATIONS.jsonl',set()):e.append(f'claim {c.get("id")} missing relation {r}')
 endpoints=ids.get('CLAIMS.jsonl',set())|ids.get('ENTITIES.jsonl',set())
 for r in recs.get('RELATIONS.jsonl',[]):
  for side in ('from','to'):
   vals=r.get(side,[]); vals=[vals] if isinstance(vals,str) else vals
   for x in vals:
    if x not in endpoints:e.append(f'relation {r.get("id")} missing endpoint {x}')
 # declared version identity
 status=(ROOT/'STATUS.md').read_text();
 if 'v1.0.0' not in status:e.append('STATUS missing v1.0.0 declaration')
 if MANIFEST.exists():
  try:m=json.loads(MANIFEST.read_text())
  except Exception as x:e.append(f'invalid manifest: {x}');m={}
  if m.get('public_version') not in {'v1.0.0','v1.0.0'}:e.append('manifest public_version invalid')
  listed={i['path']:i for i in m.get('files',[])}; actual={str(p.relative_to(ROOT)):p for p in files()}
  if set(listed)!=set(actual):e.append('manifest file allowlist differs from candidate payload')
  for rel,p in actual.items():
   if rel in listed and listed[rel].get('sha256')!=sha(p):e.append(f'manifest hash mismatch: {rel}')
 else:e.append('required release/PUBLIC_MANIFEST.json is missing')
 if e:
  print('FAIL');print('\n'.join('- '+x for x in e));return 1
 print(f'PASS: {len(files())} payload files validated; sources={len(ids.get("SOURCES.jsonl",[]))}; entities={len(ids.get("ENTITIES.jsonl",[]))}; claims={len(ids.get("CLAIMS.jsonl",[]))}; relations={len(ids.get("RELATIONS.jsonl",[]))}')
 return 0
if __name__=='__main__':sys.exit(main())
