# Soulidity source backup and computer transfer — 2026-10-12

This is a public source checkpoint and a transfer entry, not a release or a completed contract refactor. The human authorized committing and pushing the latest work for backup on 2026-10-12. This narrow authorization supersedes the older no-push wording in the preserved contract CURRENT; it does not authorize production, signatures, spending or irreversible authority changes.

## What is preserved

`repositories.json` pins fourteen checkout snapshots across thirteen public repositories: ten ecosystem modules, the contract worktree and primary project as separate Soulidity branches, a retained Animacraft checkout, and the documentation repository. Each initial checkpoint is parentless to avoid publishing unrelated local history. Existing public main/master history remains available separately. Working branches, staged work and both CURRENT continuation documents stay unchanged.

`aliases.json` records all 27 source aliases, their canonical owner repositories and byte hashes. It includes the four package-directory aliases. The contract sources still use historical absolute paths; merely cloning the repositories is insufficient until the destination layout is prepared.

`public-evidence-manifest.json` pins the latest eight candidate/acceptance checkpoints, four predecessor activation/recovery descriptors, and the exact 409 public framework inputs needed by the accepted 640-input source graph. Older public checkpoints remain in the existing Integration construction-checkpoints archives. Large generated input payloads are excluded. Every archived member retains its original bytes and historical path. The retained Animacraft v8 Move dependency closure (including Core, Output, Seal and Runtime) is included as curated source evidence; their deployed authority and complete builds are not newly accepted here. Other historical evidence fixtures retain paths to older worktrees and are not automatically runnable. Generated build trees, large execution traces, tool binaries, local chain databases, private keys and local control journals are excluded. The exclusions are explicit; this is not a backup of every local file.

New transfer guidance is English. Historical source, product decisions and evidence retain their original language and bytes.

## Contract authority and remaining work

Read `soulidity-contracts/docs/codex/PROJECT_MEMORY.md`, the preserved `docs/codex/CURRENT.md`, and its sole named handoff `docs/codex/handoffs/20261011-locked-parent-composition-actual-cutover.md`. Read the supplementary transfer handoff copied beside this file. Preserve original Owners, roadmap and Delivery/DEV/BUG records.

The accepted local-source milestone is `locked-parent-composition-activation-v1`: exact seven-file cutover, accepted actual640 readback, actual registered Market CI44, affected production and regression checks, and independent local read-only acceptance. These are source/compiler/VM results, not deployed governance, a complete Gate0/B0, an external security audit or full product acceptance.

`maker-parent-composition-activation-v1` is prepared but NOT APPLIED. Its Maker public-bridge candidate and market preflight are unactivated. Do not treat rehearsals or a backup commit as activation. The final standard-owning conformance candidate v3 has a failed test gate caused by disk exhaustion; earlier v2 passes do not accept that final candidate.

Completed Soul objects remain address-owned. Preserve authorization, supply, fund, transfer, custody, private-content and exit duties. Passive extensions/external relations must ultimately prove zero forced Market releases after a coherent B0 freeze. Original157 responsibilities, 30 duties, 1528 queue items and 15 retained maintenance units remain in scope. New Vault work is deferred; retain existing asset rights and exits.

This phase is contracts and module boundaries. Formal SDK migration and original page wiring are later product integration. Minimal unsigned callers, ABI/PTB evidence and Collection revision guards remain contract obligations.

## Restore on another computer

Install Git and Python 3.10 or newer. Clone the transfer branch from the public Integration repository:

```sh
git clone --single-branch --branch codex/backup-20261012 https://github.com/redefine-digital-labs/ecosystem-integration.git handoff-materials
cd handoff-materials/computer-transfer/2026-10-12
python3 restore_workspace.py --mode clone --destination /absolute/new/SoulidityWorkspace
python3 restore_workspace.py --mode verify --destination /absolute/new/SoulidityWorkspace
python3 restore_workspace.py --mode prepare --destination /absolute/new/SoulidityWorkspace
```

Use `destination/repositories/soulidity-contracts` as the continuation working checkout, and keep this transfer package available beside it. Absolute roots in the preserved CURRENT describe the original machine; use the repository mapping and relocation receipt for the new machine. Use a fresh destination. `clone` checks out the pinned initial source commits, including the Integration source checkpoint preceding this additive transfer package. `verify` checks original file bytes, modes and symlink targets. `prepare` verifies and installs archive members, restores portable owner links, and rewrites local path prefixes in active Move.toml dependency manifests while preserving read-only file permissions. Frozen output/evidence manifests and guard scripts retain their original bytes. It writes a relocation receipt. Path normalization intentionally changes those destination manifest bytes; retain the receipt and the untouched public checkpoints. Run original-byte verification before preparation, not after it.

The commands do not build, sign, deploy, replay chain transactions or change production permissions. They have not run on the recipient computer. Before contract work resumes, verify the Sui compiler/toolchain and rebuild fresh evidence from the relocated graph. The prior tool baseline is Sui1.80.1 and framework revision `2a0becb2fcc6989e492981104af67f62f2c9511a`; the historical Mac executable hash is not a cross-platform acceptance.

Frozen historical guard scripts pin old absolute paths and CURRENT versions. Do not execute old cutover or rollback scripts against the relocated workspace. Build a fresh reviewed plan and guards after restoring the new workspace; historical receipts remain evidence of the original machine. The v6→v5 continuation restoration and exact7 rollback ordering remain historical recovery facts, not authorization to perform rollback.

## Private/offline transfer still required

For work requiring retained local chain state, use a separate protected transfer of chain databases/genesis/keys, wallet access, `.cas` journals and necessary tool binaries. They are not on public GitHub. Existing browser drafts and unrelated/historical worktrees are not reproduced by this source restore. Keep the old computer's files until destination verification and the necessary private transfer pass. Never replay the retained Community publication or issue fresh signatures as a way to reconstruct its state.

The nested Animacraft checkpoint is retained historical source, not the currently deployed BUG006 frontend authority. Its accepted production commit and other active production worktree remain described in the primary CURRENT handoff. No production deployment or browser/wallet migration happened in this backup.

## Resume prompt

> Continue the Soulidity contract/module refactor from this transfer package. First restore and verify the pinned sources, owner aliases, exact framework inputs and relocation receipt. Read the preserved contract PROJECT_MEMORY, CURRENT and sole handoff, then the supplementary transfer handoff. Keep original157/30/1528/15 responsibilities, Owners, roadmap and records. H1 exact7 is accepted local source; H2 Maker activation is unperformed; the final Standard conformance gate remains failed. Do not reuse frozen absolute-path cutover scripts. Prepare fresh source/ABI/Cap/type/authority guards on this computer, then finish the Maker public bridge and genuine Manufacturing-only parent composition, independently review its activation, and integrate canonical owning conformance tests. Continue Gate0 and coherent B0, permissions/upgrades/exits and passive compatibility proofs. This scope is contracts; SDK/page integration remains later. Do not deploy production, sign transactions, spend funds, change irreversible permissions, merge production branches, replay publication or delete old data without explicit authorization. A source backup does not complete the full refactor.

## Verification

All fourteen initial source refs were verified against GitHub. Independent review checked the complete 8,921-file source trees, working Git guards and canonical alias coverage. The restore helper passed a synthetic full clone/verify/prepare fixture, including disabled global symlinks, source drift refusal and source-root overlap refusal. This package does not certify execution on the recipient machine. See the JSON receipts and reviews beside this file.
