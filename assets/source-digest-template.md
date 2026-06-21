# Source Digest Template

Use this template to convert a short, user-provided source excerpt into an auditable source摘要卡. A Source Digest is a provenance record and hypothesis input for supply-chain chokepoint research; it is not an investment conclusion, not a Serenity official statement, and not a confirmed supply-chain chokepoint finding.

## Source type labels

Choose one primary label and keep mixed materials separated:

- **Serenity original public expression**: a short excerpt that is plausibly Serenity's own public wording, with enough locator information for later review.
- **Community interpretation**: a forum, social-media, newsletter, or other third-party interpretation of Serenity, an industry theme, or a company claim.
- **User-provided note**: the user's own summary, transcription, screenshot text, or unsourced note; unverified until independently checked.
- **Supply-chain evidence**: company disclosures, filings, earnings-call transcripts, industry data, standards documents, or other materials that can support or challenge a supply-chain mechanism.
- **Assistant inference**: the assistant's bounded interpretation, research hypothesis, uncertainty note, missing checks, or next-step design.

Do not merge these labels. For example, a community post discussing Serenity remains **community interpretation**, not Serenity original public expression; a company disclosure remains **supply-chain evidence**, not a confirmed 供应链卡点 conclusion.

## Copyable template

```markdown
# Source Digest: <digest_id>

| Field | Entry |
| --- | --- |
| digest_id | SD-YYYYMMDD-001 |
| source_type | Choose one: Serenity original public expression / community interpretation / user-provided note / supply-chain evidence / assistant inference. If mixed, split into separate digests. |
| source_title | Short title supplied by the user or derived neutrally from the locator. |
| source_url_or_locator | URL, filing locator, transcript name, document section, screenshot provenance note, or `unavailable` if unavailable. Do not add cookies, API keys, session files, or private locators. |
| source_date | Publication / event date if known; otherwise `unknown`. |
| collection_date | Date the user supplied or the assistant reviewed the excerpt. |
| provided_by | User / public filing / company disclosure / transcript provider / other stated provider. |
| original_excerpt | Short excerpt only. Preserve quotation boundary and do not store long third-party original text. |
| excerpt_length_note | State why the excerpt is short enough for review, or note that it must be shortened before storage. |
| paraphrase | Neutral paraphrase of the excerpt, without strengthening the claim. |
| translation_note | If translated, state source language, target language, and whether this is a literal translation or paraphrase. If no translation, write `not translated`. |
| attribution | Who said / published / interpreted the material, and what remains unverified. |
| claim_extracted | The narrow claim that can be extracted from the excerpt. Use cautious language such as `suggests`, `states`, `claims`, or `reports`. |
| claim_scope | Scope boundary: product, component, process step, geography, time period, customer segment, or `unspecified`. |
| supports | What candidate research hypothesis this source may support, if any. Use `hypothesis input only` when relevant. |
| contradicts | Any direct contradiction, limitation, or counter-signal visible in the excerpt. Use `none in excerpt` if absent. |
| interpretation_boundary | Explicitly separate original wording, paraphrase, translation, community interpretation, supply-chain evidence, and assistant inference. |
| evidence_level | L0-L5, using the project's evidence ladder. User notes and community interpretations are normally low-level inputs until checked. |
| confidence | low / medium / high confidence in the extracted claim, not in an investment outcome. |
| missing_checks | Verification steps needed before the source can affect a 供应链卡点分析 evidence table. |
| allowed_use | Permitted use, e.g., provenance record, hypothesis seed, evidence-table input after checks, or wording clarification. |
| disallowed_use | Prohibited use, e.g., investment advice, trade instruction, Serenity endorsement, confirmed chokepoint proof, or bulk content archive. |
| next_research_step | One concrete next step, such as obtain primary filing, compare transcript, check capacity data, or look for counterevidence. |
| non_investment_advice_note | This digest is for supply-chain chokepoint research workflow design only; it is not investment advice, a buy/sell instruction, or a return promise. |
```

## Quality checklist

Before using a Source Digest as an input to a chokepoint evidence table, confirm:

1. The source label is explicit and does not convert community interpretation into Serenity original public expression.
2. The original excerpt is short, attributed, and separated from paraphrase, translation, and assistant inference.
3. The claim is narrow enough to audit and does not overstate shortage, social-media heat, or management commentary as a confirmed 供应链卡点.
4. Missing checks include primary-source verification, counterevidence, substitution risk, capacity expansion, customer validation, time horizon, and invalidation conditions where relevant.
5. The digest does not contain cookies, API keys, sessions, private research material, bulk third-party text, real company conclusions, investment advice, trade instructions, or return promises.