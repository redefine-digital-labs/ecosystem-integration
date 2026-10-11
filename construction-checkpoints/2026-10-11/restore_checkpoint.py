from pathlib import Path
import hashlib,json,runpy,sys,tarfile
r=Path(__file__).resolve().parent
if len(sys.argv)!=2: raise SystemExit('Usage: python3 restore_checkpoint.py NEW_DESTINATION')
dest=Path(sys.argv[1]).resolve()
if dest.exists(): raise SystemExit('Destination already exists; choose a new isolated directory.')
runpy.run_path(str(r/'verify_archives.py'))
overlay=json.loads((r/'CONTINUATION_OVERLAY.json').read_text())
for name,row in overlay.items():
 assert hashlib.sha256((r/name).read_bytes()).hexdigest()==row['sha256'],name
 assert not Path(row['target']).is_absolute() and '..' not in Path(row['target']).parts
locations={'reconstruction-worktree-source.tar.gz':'reconstruction','original-construction-inputs.tar.gz':'construction-inputs','maker-source-lookup-ad70.tar.gz':'candidates/maker-source-lookup-ad70','independent-market-3225.tar.gz':'candidates/independent-market-3225','construction-evidence.tar.gz':'evidence'}
for archive,folder in locations.items():
 with tarfile.open(r/archive) as t:
  for member in t.getmembers():
   assert member.isfile() and not Path(member.name).is_absolute() and '..' not in Path(member.name).parts
   p=dest/folder/member.name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.extractfile(member).read())
for name,row in overlay.items():
 p=dest/'reconstruction'/row['target'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((r/name).read_bytes())
print('Restored source/evidence and latest continuation into',dest)
print('Candidates remain separate and inactive. Clone soul-sdk separately for its latest SDK candidate. No keys, chain DBs or CLI binaries were restored.')
