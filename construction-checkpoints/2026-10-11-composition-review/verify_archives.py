from pathlib import Path
import json,hashlib,tarfile
r=Path(__file__).resolve().parent
for p in sorted(r.glob('*.manifest.json')):
 m=json.loads(p.read_text());a=r/m['archive']
 assert hashlib.sha256(a.read_bytes()).hexdigest()==m['archive_sha256'],a.name
 with tarfile.open(a) as t:
  members=t.getmembers();assert len({x.name for x in members})==len(members)
  assert all(x.isfile() and not x.name.startswith('/') and '..' not in Path(x.name).parts for x in members)
  actual={x.name:hashlib.sha256(t.extractfile(x).read()).hexdigest() for x in members}
 assert actual==m['member_sha256'],a.name
 print(a.name,len(actual),'PASS')
