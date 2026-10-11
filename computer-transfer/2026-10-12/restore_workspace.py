#!/usr/bin/env python3
"""Restore a source checkpoint into a new directory; never sign, deploy or delete."""
import argparse, hashlib, io, json, os, subprocess, tarfile, tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent

def sha(data):return hashlib.sha256(data).hexdigest()
def read(name):return json.loads((HERE/name).read_text())
def git(root,*args):
 return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.PIPE).decode().strip()
def file_bytes(p):return os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--destination',type=Path,required=True)
 parser.add_argument('--mode',choices=['clone','verify','prepare'],default='verify')
 args=parser.parse_args();base=args.destination.resolve()
 metadata=read('repositories.json');rows=metadata['repositories']
 for row in rows:
  old=Path(row['original_root']).resolve()
  if base.is_relative_to(old) or old.is_relative_to(base):raise RuntimeError('Destination overlaps an original workspace: '+str(old))
 roots={r['id']:base/'repositories'/r['id'] for r in rows}
 report={'mode':args.mode,'source_backup_is_not_release':True,'repositories':[],'transforms':[]}
 for r in rows:
  root=roots[r['id']]
  if args.mode=='clone':
   if root.exists():raise RuntimeError('Refusing existing destination: '+str(root))
   root.parent.mkdir(parents=True,exist_ok=True)
   subprocess.run(['git','clone','-c','core.symlinks=true','--single-branch','--branch',r['ref'].removeprefix('refs/heads/'),r['clone_url'],str(root)],check=True)
   subprocess.run(['git','-C',str(root),'checkout','--detach',r['commit']],check=True)
  assert git(root,'rev-parse','HEAD')==r['commit'],r['id']+' wrong checkpoint'
  for name,want in r['files'].items():
   p=root/name;assert p.exists() or p.is_symlink(),r['id']+'/'+name+' missing'
   assert sha(file_bytes(p))==want['sha256'],r['id']+'/'+name+' source bytes differ'
   mode='120000' if p.is_symlink() else ('100755' if p.stat().st_mode&0o111 else '100644')
   assert mode==want['mode'],r['id']+'/'+name+' mode differs'
  report['repositories'].append({'id':r['id'],'commit':r['commit'],'verified_files':len(r['files'])})
 if args.mode=='prepare':
  receipt=base/'relocation-receipt.json'
  if receipt.exists():raise RuntimeError('Preparation already recorded; preserve receipt and use a fresh destination for replay')
  evidence=read('public-evidence-manifest.json');data=b''
  for part in evidence['archives']:
   chunk=(HERE/part['path']).read_bytes();assert sha(chunk)==part['sha256'];data+=chunk
  wanted={r['archive_path']:r for r in evidence['files']}
  with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as tar:
   members=tar.getmembers();assert {m.name for m in members}==set(wanted)
   for member in members:
    assert member.isfile() and '..' not in Path(member.name).parts and not Path(member.name).is_absolute()
    row=wanted[member.name];payload=tar.extractfile(member).read();assert sha(payload)==row['sha256']
    assert member.name==row['repository']+'/'+row['path']
    relative=Path(row['path']);assert not relative.is_absolute() and '..' not in relative.parts
    target=roots[row['repository']]/relative;root=roots[row['repository']].resolve()
    assert target.parent.resolve().is_relative_to(root) and not target.is_symlink(),'Archive target escapes destination owner'
    assert target.is_relative_to(roots[row['repository']])
    if target.exists():assert target.read_bytes()==payload,'Refusing to overwrite different bytes: '+str(target)
    else:
     target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(payload);target.chmod(row['mode'])
  for link in read('aliases.json')['aliases']:
   target=roots[link['owner_repository']]/link['owner_path'];path=roots[link['repository']]/link['path']
   assert path.is_symlink() and os.readlink(path)==link['original_target']
   if link['target_file_sha256']:assert sha(target.read_bytes())==link['target_file_sha256']
   else:
    for name,digest in link['target_directory_files'].items():assert sha((target/name).read_bytes())==digest
   replacement=os.path.relpath(target,path.parent)
   path.unlink();path.symlink_to(replacement)
   report['transforms'].append({'repository':link['repository'],'path':link['path'],'kind':'symlink','before':link['original_target'],'after':replacement})
  replacements=sorted(((r['original_root'],str(roots[r['id']])) for r in rows),key=lambda v:len(v[0]),reverse=True)
  for identity,root in roots.items():
   for folder,dirs,files in os.walk(root,followlinks=False):
    dirs[:]=[d for d in dirs if d not in {'.git','node_modules','build','traces','output','evidence','construction-checkpoints','computer-transfer'} and not (Path(folder)/d).is_symlink()]
    if 'Move.toml' not in files:continue
    path=Path(folder)/'Move.toml'
    if path.is_symlink():continue
    before=path.read_bytes();after=before
    for old,new in replacements:after=after.replace(old.encode(),new.encode())
    if after!=before:
     mode=path.stat().st_mode&0o777
     descriptor,temporary=tempfile.mkstemp(prefix='.soul-path-',dir=path.parent)
     with os.fdopen(descriptor,'wb') as out:out.write(after)
     os.chmod(temporary,mode);os.replace(temporary,path)
     report['transforms'].append({'repository':identity,'path':path.relative_to(root).as_posix(),'kind':'Move manifest local paths','before_sha256':sha(before),'after_sha256':sha(after),'mode_preserved':mode})
  report['historical_frozen_guards_not_rebased']=True
  report['chain_keys_and_databases_not_restored']=True
  receipt.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps(report,indent=2,sort_keys=True))
if __name__=='__main__':main()
