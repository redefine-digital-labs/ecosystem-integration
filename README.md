# ecosystem-integration

INTEGRATION: Composition verification and external integration evidence. Exact combinations, consumer choices, interoperability, and takeover reports.

Maintenance entry points: [MODULE](MODULE.md), [Agent boundaries](AGENTS.md), [Compatibility](COMPATIBILITY.md), [Operation and recovery](RUNBOOK.md). Machine configuration: [module.json](module.json).

Actual construction: boundaries and maintenance contracts exist; cross-repository journey implementations have not yet moved here. See module.json for detailed evidence status; independent deployment and remote CI have not been accepted.
Recommended role: FLUX; the original Owner is unchanged. Unconfirmed actual maintainers and independent acceptors remain pending; role names are not accounts or audit qualifications.

```sh
python3 scripts/ci.py
python3 scripts/ci.py --product
python3 scripts/ci.py --release-ready
```

Default CI checks maintenance contracts; `--product` refuses to pass when product commands are unregistered. Readiness gates do not deploy or sign.

## Current checkpoint

See [construction status](CONSTRUCTION_STATUS.md) for current evidence, blockers, recovery material and remote coordination. This checkpoint is not a release.
