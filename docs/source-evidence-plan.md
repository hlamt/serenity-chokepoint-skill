# V0.3 Source Evidence Plan

## Purpose

This plan defines the V0.3 source boundary for serenity-chokepoint-skill. It explains how the Skill may use Serenity public expression, supply-chain evidence, and community interpretation when forming supply-chain chokepoint research hypotheses.

The plan is intentionally limited to source handling. It does not authorize X scraping, twscrape integration, automated social-media collection, external API calls, real company conclusions, investment advice, trade instructions, or return promises.

## Source boundary

The Skill may use traceable public sources and user-provided excerpts only when the source type is labeled and the evidence chain remains reviewable. Every claim should separate:

1. **Serenity public expression**: what Serenity publicly expressed in the provided or cited source.
2. **Supply-chain evidence**: filings, disclosures, transcripts, industry data, and other industry-chain materials.
3. **Community interpretation**: user notes, translations, summaries, or secondary commentary about Serenity or an industry theme.
4. **Assistant inference**: the Skill's research hypothesis, confidence level, risks, tracking indicators, and invalidation conditions.

## Allowed source types

Allowed sources include short, traceable excerpts or citations from:

- Primary public expression.
- Company disclosure.
- Regulatory filing.
- Earnings call transcript.
- Industry report.
- Market data.
- News article.
- Social media post supplied by the user or accessed under an explicit future authorization gate.
- Community interpretation, clearly labeled as interpretation.
- User-provided note, clearly labeled as user-provided and unverified until checked.

Use [references/source-types.md](../references/source-types.md) for evidence strength, risks, and whether each source can independently support a supply-chain chokepoint claim.

## Disallowed source types

Do not use or request:

- Private messages, leaked content, paywalled bulk archives, cookies, session tokens, API keys, or other secrets.
- Unattributed screenshots or copied text where provenance cannot be checked.
- Bulk downloads of third-party original content.
- Automated X scraping, twscrape output, or external API results unless a future authorization gate explicitly permits the workflow and compliance checks.
- Community translations presented as if they were Serenity's original words.
- Synthetic statements that impersonate Serenity or imply official endorsement.

## Serenity public expression handling

Serenity is treated as a public framework source, not as an investment signal oracle. The Skill may use Serenity public expression to understand framework vocabulary, source-boundary habits, and chokepoint reasoning patterns, but not to imply an official signal, endorsement, or guaranteed investment outcome.

Rules:

- Keep Serenity's original expression separate from user interpretation, community interpretation, and assistant inference.
- Attribute Serenity public expression to the specific source supplied or cited.
- Do not infer Serenity's private intent, unpublished view, position, portfolio, or current opinion.
- Do not impersonate Serenity or write in a way that claims to be Serenity.
- Do not state or imply that this project is officially authorized, endorsed, reviewed, or approved by Serenity.

## Quotation and paraphrase policy

- Prefer paraphrase with attribution when a concept can be summarized without losing meaning.
- Use short quotations only when necessary to preserve terminology, framing, or disputed wording.
- Quote only the minimum necessary excerpt and keep quotation boundaries visible.
- Never rewrite Serenity expression into a stronger claim than the source supports.
- Translations must be labeled as translations or paraphrases, not original Serenity claims.
- If wording is ambiguous, state the ambiguity and list what evidence would resolve it.

## Evidence storage boundary

The repository may store lightweight metadata, short excerpts needed for review, and user-authored summaries. It must not store large third-party corpora, bulk social-media archives, cookies, API keys, session files, or private research material.

Recommended stored fields:

- source type;
- source title or short description;
- source URL or provenance note;
- date observed and publication date when available;
- short excerpt or paraphrase;
- claim supported, contradicted, or left unresolved;
- evidence level and confidence;
- risks, tracking indicators, and invalidation conditions.

## Manual collection workflow

1. Confirm the research question and system boundary.
2. Label each supplied item by source type before analysis.
3. Separate Serenity public expression, community interpretation, supply-chain evidence, and assistant inference.
4. Record source date, provenance, and excerpt boundary.
5. Build an evidence table that distinguishes support, counterevidence, uncertainty, and missing checks.
6. Form only research hypotheses about candidate supply-chain chokepoints.
7. Include risk list, tracking indicators, and invalidation conditions.
8. State the non-investment-advice boundary.

## Automated collection preconditions

Automated collection is out of scope for V0.3. Before any future automation is enabled, the project must define and review:

- explicit user authorization level and collection target;
- source terms-of-service and legal/compliance boundary;
- rate limits and robots or platform restrictions where applicable;
- data minimization plan and retention boundary;
- secrets handling plan that avoids storing cookies, API keys, or sessions in the repo;
- deduplication and provenance tracking;
- quotation-length controls and copyright-aware excerpting;
- manual review checkpoint before generating any real company research conclusion.

## L0 / L1 / L2 authorization gates

- **L0 local documentation**: edit docs, references, evals, and scripts; run local validation; no network collection; no X scraping; no external API calls.
- **L1 GitHub cloud modification**: create branches, commit, push, and open pull requests for repository changes. This may use GitHub transport only for repository operations and still does not authorize X scraping, twscrape, cookies, secrets, external data APIs, or real company conclusions.
- **L2 data collection design or execution**: requires explicit future authorization naming the source, method, storage boundary, compliance checks, and allowed output. L2 is not granted by V0.3 documentation work.

## Non-investment-advice boundary

The Skill outputs supply-chain chokepoint research hypotheses for investment researchers and industry-chain analysts. It must not output investment advice, buy/sell instructions, position sizing, personalized recommendations, return promises, or claims that a public expression predicts a trade outcome.