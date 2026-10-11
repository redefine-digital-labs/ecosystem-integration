# English repository-generator candidate

Candidate: `generate.py`. Original source remains untouched. Root is the sole installer.

Verification: PASS. Python AST syntax passed; all executable AST structure is identical except 28 explicitly bounded owned-prose string constants. Keys, numeric literals, identifiers, conditionals, calls, statuses, schema, links, shell commands and historical lookup key `关联原研发／Bug` are preserved. All ten module configurations and 50 Markdown documents rendered through the unchanged pure functions. The generation CLI and remote CI were not run.

- Original SHA-256: `6a23f0e2b60dca8ef488009931061aa5e4669df4ace67762b08cf9ac586c8d4b`
- Candidate SHA-256: `d0a3cfc9a971137c6b8d0c1fa931a630a3a7309c51efe32165a85ae4dc9b0b54`
- Evidence: `verification.json`, `generator-prose.diff`, `original-pin.json`.
- Reproduce before installation: `python3 verify_candidate.py`.
- Actual DEVOPS sample: `rendered-verification/` (verification output only).

Generator-owned prose is English. Imported values from immutable Chinese JSON are preserved verbatim. 10 of 10 configurations retain imported Chinese; 20 of 50 rendered documents retain imported Chinese. The exact paths and affected documents are inventoried in `verification.json`; this candidate does not claim those imported strings were translated.

Handbook v1.0 (2026-10-06), sections 1–4, 5, 9 and 12 applied to the bounded Code/Test candidate. Remaining checks: Root review/installation and attachment to the existing original record. No Git, remote, source, frozen-evidence or CURRENT mutation occurred.
