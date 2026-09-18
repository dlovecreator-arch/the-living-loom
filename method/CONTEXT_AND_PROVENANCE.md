# Context and provenance

The Loom remembers broadly but attends selectively.

## Three memory layers

- **Archive:** raw artifacts, exact records, historical ledgers, prior models, and dormant clues.
- **Current state:** the active method, current model, open knots, source frontier, and forecast state.
- **Working set:** only the evidence needed for the present question.

A summary must never become the only surviving representation of a source family. The public edition is a selected working projection, not the archive itself.

## Authority order

Raw artifact → verified exact record → current canonical decision → older synthesis → conversation summary → model memory.

## Public claim fields

Each record in `research/CLAIMS.jsonl` contains:

- `id`, `label`, `text`;
- `origin` and `claim_kind`;
- `status` and `review_state`;
- `source_refs` and `relation_refs`;
- `rivals_or_limits`;
- `revision`.

Origin and evidential status are separate. A claim can be explicit in a source while remaining externally unverified.

Each relation in `research/RELATIONS.jsonl` contains `id`, `from`, `to`, `type`, `basis`, `conditions`, `limits`, `origin`, and `review_state`. Analogy, chronology, causality, identity, and shared language are not interchangeable relation types.

## Public evidence states

- `public_locator_verified`: a reviewed public route is available.
- `public_locator_unavailable`: this release provides no reviewed public route.
- `limited_access`: this release provides only a source description and stated limits—not the underlying wording, media, or a reproducible derivation.

Locator status and access status are separate and may both apply to one source. Neither `public_locator_unavailable` nor `limited_access` is public verification.
