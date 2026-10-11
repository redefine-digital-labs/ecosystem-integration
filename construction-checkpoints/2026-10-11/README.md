# Construction checkpoint — 2026-10-11

These repositories are independently owned maintenance units under construction. Repository creation and remote backup do not prove independent deployment or completion of the original product. Existing Owners, Delivery/DEV/BUG records and the 15 retained maintenance units remain authoritative.

The latest Maker source-lookup candidate is NOT_INSTALL_READY: the exact whole-Core local run passed 1061 of 1062 tests; the original post-mint supply rejection still exhausts the default VM budget. Maker's 49 scoped tests pass. The original matching publication baseline passed 52 of 52. No budget or test loop was increased.

The independent Market candidate has a separate paired graph: 44 Market tests, six passive-extension journeys and five Standard tests pass; all 194 production module bytes remain unchanged across the passive-extension proof. Do not merge this graph's evidence with the later Maker candidate.

The SDK candidate passes 35 isolated tests and a Root independently executed targeted typecheck. It is NOT_ACTIVATED / NOT_INSTALL_READY: original UI activation, automatic custody-account pairing, repricing, actual chain execution and final B0 acceptance remain pending. Channel runtime implementation and complete cross-module acceptance remain unfinished.

GitHub Actions are disabled during the backup checkpoint. Workflow templates are not evidence of remote CI, release or deployment. Active public module documents and new coordination materials use English. Immutable original source and historical evidence retain their original bytes and language for hash verification. Original project contributions use MIT; third-party code retains its upstream licenses.

[Recovery archives and manifests](https://github.com/redefine-digital-labs/ecosystem-integration/tree/main/construction-checkpoints/2026-10-11) · [Coordination registry](https://github.com/redefine-digital-labs/ecosystem-integration/blob/main/construction-checkpoints/2026-10-11/REMOTE_COORDINATION.json)

## Restore

Clone the ten public repositories listed in REMOTE_COORDINATION.json. Verify every archive with its adjacent manifest, then extract into a new isolated directory. Restore the reconstruction worktree and candidates as separate directories; never copy a failed candidate over installed authority. Local absolute paths in original manifests are provenance, not mandatory restore destinations. Pinned Sui CLI identity: v1.80.1-671ba71e69c7, SHA256 1d7baa7c7314113671415acfa20279b1eedb6ae6d04f286988a00da285e769c3. Binaries, credentials and chain databases must be supplied separately; no live deployment is reproduced by these archives.

Use verify_archives.py before extraction. It verifies compressed file hashes, all member hashes and rejects traversal or symlink entries. Keep the paired Market graph separate from the later Maker source-lookup graph. Follow the English CURRENT and handoff for the next authorized action.
