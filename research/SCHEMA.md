# Public machine-record schema

Schema version: **2.0**. This schema version is separate from the public release version and from the private Loom engine version.

Each `.jsonl` file contains one JSON object per line. Unknown values remain `null` or are described explicitly; absence is not silently converted into certainty.

## `SOURCES.jsonl`
Required fields: `id`, `label`, `author_role`, `source_kind`, `date_text`, `date_status`, `channel_completeness`, `locator_status`, `public_url` (nullable), `access_status`, `human_index_anchor`, `review_state`.

## `ENTITIES.jsonl`
Required fields: `id`, `label`, `entity_kind`, `origin`, `definition`, `limits`.

## `CLAIMS.jsonl`
Required fields: `id`, `label`, `text`, `origin`, `claim_kind`, `status`, `source_refs`, `relation_refs`, `rivals_or_limits`, `revision`, `review_state`. `source_refs` resolve to source IDs; `relation_refs` resolve to relation IDs.

## `RELATIONS.jsonl`
Required fields: `id`, `from`, `to`, `type`, `basis`, `conditions`, `limits`, `origin`, `review_state`. `from` and `to` may be a single ID or an array. Every endpoint must resolve to a public claim or declared entity. A grouping relation does not establish causation or identity.
