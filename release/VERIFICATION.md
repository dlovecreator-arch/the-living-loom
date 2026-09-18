# Release verification — v1.0.0

Verification date: **18 September 2026**  
Payload status: **PASS — final public baseline**

This receipt records checks actually performed on the exact local v1.0.0 payload before publication. Publication/readback is recorded separately in the private canonical closeout receipt because publishing occurs after this payload and its hashes are fixed.

## Results

| Check | Result | Observation / limit |
| --- | --- | --- |
| Public schema and reference integrity | PASS | `scripts/validate_release.py` passed with 37 payload files, 9 source records, 1 entity record, 10 claims and 2 relations; all declared references resolved. |
| Markdown links and fragments | PASS | Validator checked local Markdown targets and heading fragments. |
| Manifest equality and SHA-256 hashes | PASS | `release/PUBLIC_MANIFEST.json` was rebuilt from the final payload and the exact payload passed hash/readback validation. The manifest intentionally excludes its own hash. |
| Public/private boundary | PASS | Validator scanned public text for private Drive/source-route patterns defined by the release boundary. Raw screenshots, private Drive routes, active unscored forecasts and closeout-control records are not in the allowlisted tree. |
| Negative machine fixtures | PASS | Deliberate missing source ID, missing relation endpoint, duplicate ID, invalid field type and broken Markdown fragment each caused validator failure for the intended reason. |
| Late-corpus source fidelity | PASS at stated scope | Preserved raw screenshots supporting the new Foundations discussion of the labyrinth account (SRC-LL-0090), bucket account (SRC-LL-0099), affect/logic sequence (SRC-LL-0103) and practice passage (SRC-LL-0111) were visually rechecked. This does not recover missing channels or verify metaphysical claims. |
| Public locator search | COMPLETE / NO VERIFIED LOCATOR FOUND | A bounded search found no sufficiently verified public copy for the newly used late-corpus passages. Records therefore remain `public_locator_unavailable` / `limited_access`; no substitute URL was invented. |
| Public bundle only | PASS, context-informed inspection | README and START_HERE provide purpose, inspectable-example route, standalone starter, status, rights and correction path without requiring private access. |
| Standalone starter | PASS, context-informed behavior check | Starter explicitly denies private-corpus access, requires supplied evidence, preserves rivals and attribution, and includes a complete original demonstration. |
| Missing continuation challenge | PASS | Starter and inspectable example explicitly require the absent paragraph/source to be supplied rather than invented. |
| Symbol-collapse challenge | PASS | The blue-object example rejects the inference that shared color is a universal key and retains a rival practical-reading account. |
| Detour challenge | PASS | Public method distinguishes local direction from route progress and explicitly rejects the rule that every setback is progress without route evidence. |
| Attribution challenge | PASS | Synthetic demonstration is labeled original; Dana-derived commentary is separated from Loom interpretation and new design. |
| Forecast integrity | PASS on private closeout authorities | PRED-134–150 remain 17 distinct frozen records; PRED-147 is excluded from already-exposed Playbook trials and PRED-148–150 are excluded from completed corpus evidence. Forecasts are not published in this public payload. |
| Private recovery identity set | PASS on private Drive-native mirror | All 558 inventoried original Drive IDs resolve in the recovery mirror: 432/432 Living Loom research/history files and 126/126 Dana raw-batch objects. This is a Drive-native recovery mirror, not a claim of a fully offline byte archive. |

## Not run / not claimed

No human usability study, phone-layout test, TTS playback test, independent model benchmark, Dana-intent verification, complete public-permalink recovery, or external validation of extraordinary/metaphysical mechanisms was performed. The release does not claim any of those things.

The public edition is therefore complete for its declared purpose: an inspectable commentary/method baseline with explicit evidence limits, not a complete public reproduction of the private corpus.
