import hashlib,io,json,os,subprocess,tarfile,tempfile
from pathlib import Path
SCRIPT=Path('restore_workspace.py').resolve()
def sha(x):return hashlib.sha256(x).hexdigest()
with tempfile.TemporaryDirectory(prefix='soul-transfer-fixture-') as folder:
 base=Path(folder);material=base/'materials';material.mkdir();(material/'restore_workspace.py').write_bytes(SCRIPT.read_bytes())
 owner=base/'original-owner';consumer=base/'original-consumer';rows=[]
 def git(p,*a):return subprocess.check_output(['git','-C',str(p),*a],stderr=subprocess.DEVNULL).decode().strip()
 for identity,root in [('owner',owner),('consumer',consumer)]:
  root.mkdir();git(root,'init');git(root,'config','user.name','Fixture');git(root,'config','user.email','fixture@example.invalid');git(root,'config','core.symlinks','true')
  if identity=='owner':
   (root/'pkg').mkdir();(root/'pkg/source.move').write_text('module fixture::source {}\n');(root/'pkg/Move.toml').write_text('[dependencies]\nDep = { local = "'+str(root)+'/.deps/core" }\n')
   (root/'evidence').mkdir();(root/'evidence/Move.toml').write_text('[dependencies]\nOld={local="'+str(root)+'/historical"}\n')
  else:
   (root/'package').symlink_to(owner/'pkg',target_is_directory=True);(root/'source.move').symlink_to(owner/'pkg/source.move')
  git(root,'add','.');git(root,'commit','-m','fixture');git(root,'branch','codex/fixture');files={}
  for name in git(root,'ls-files').splitlines():
   p=root/name;data=os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
   files[name]={'sha256':sha(data),'mode':'120000' if p.is_symlink() else '100644','bytes':len(data)}
  rows.append({'id':identity,'clone_url':str(root),'ref':'refs/heads/codex/fixture','commit':git(root,'rev-parse','HEAD'),'original_root':str(root),'files':files})
 (material/'repositories.json').write_text(json.dumps({'repositories':rows}))
 aliases=[]
 for name in ['package','source.move']:
  isdir=name=='package';target=owner/'pkg' if isdir else owner/'pkg/source.move'
  aliases.append({'repository':'consumer','path':name,'original_target':str(target),'owner_repository':'owner','owner_path':'pkg' if isdir else 'pkg/source.move','target_file_sha256':None if isdir else sha(target.read_bytes()),'target_directory_files':{k.removeprefix('pkg/'):v['sha256'] for k,v in rows[0]['files'].items() if k.startswith('pkg/')} if isdir else {}})
 (material/'aliases.json').write_text(json.dumps({'aliases':aliases}))
 data=('[package]\nname="fixture"\n[dependencies]\nOther={local="'+str(owner)+'/pkg"}\n').encode();archive=material/'fixture.tar.gz';name='owner/.deps/core/Move.toml'
 with tarfile.open(archive,'w:gz') as tar:
  info=tarfile.TarInfo(name);info.size=len(data);tar.addfile(info,io.BytesIO(data))
 (material/'public-evidence-manifest.json').write_text(json.dumps({'archives':[{'path':archive.name,'sha256':sha(archive.read_bytes())}],'files':[{'archive_path':name,'repository':'owner','path':'.deps/core/Move.toml','sha256':sha(data),'mode':292}]}))
 config=base/'global-config';config.write_text('[core]\n symlinks = false\n');env={**os.environ,'GIT_CONFIG_GLOBAL':str(config)};destination=base/'new-workspace'
 for mode in ['clone','verify','prepare']:
  p=subprocess.run(['python3',str(material/'restore_workspace.py'),'--destination',str(destination),'--mode',mode],capture_output=True,env=env)
  assert p.returncode==0,p.stderr.decode()
 assert (destination/'repositories/consumer/package/source.move').read_bytes()==(owner/'pkg/source.move').read_bytes()
 assert str(destination/'repositories/owner').encode() in (destination/'repositories/owner/pkg/Move.toml').read_bytes()
 cache=destination/'repositories/owner/.deps/core/Move.toml'
 assert str(destination/'repositories/owner').encode() in cache.read_bytes()
 assert cache.stat().st_mode&0o777==0o444
 assert git(destination/'repositories/owner','config','core.symlinks')=='true'
 assert (destination/'repositories/owner/evidence/Move.toml').read_bytes()==(owner/'evidence/Move.toml').read_bytes()
 receipt=json.loads((destination/'relocation-receipt.json').read_text());assert len(receipt['transforms'])==4
 bad=subprocess.run(['python3',str(material/'restore_workspace.py'),'--destination',str(owner),'--mode','prepare'],capture_output=True,env=env);assert bad.returncode!=0
 (destination/'repositories/owner/pkg/source.move').write_text('unexpected drift')
 drift=subprocess.run(['python3',str(material/'restore_workspace.py'),'--destination',str(destination),'--mode','verify'],capture_output=True,env=env);assert drift.returncode!=0
 print('PASS clone/byte+mode verification, global-symlinks=false override, directory/file aliases, archive byte hashes, Move path relocation receipt including readonly0444 permission preservation, frozen evidence unchanged, overlap refusal and unknown source drift refusal')
