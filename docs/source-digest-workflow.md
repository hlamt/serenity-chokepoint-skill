# Source Digest Workflow

## Purpose

The Source Digest workflow turns a short, user-provided source excerpt into an auditable source摘要卡 for 供应链卡点研究. Its purpose is provenance control: preserve what was provided, label what kind of source it is, extract only the narrow claim supported by the excerpt, and list missing checks before the material can enter a later evidence chain.

A Source Digest is not an investment conclusion, not a Serenity official viewpoint statement, and not a confirmed supply-chain chokepoint finding. It is only a structured input for later research.

## When to use

Use this workflow when the user provides a short source excerpt or locator, such as:

- a short Serenity public expression;
- a community interpretation or translation;
- a user-provided note or screenshot transcription;
- a company announcement, filing excerpt, or transcript excerpt;
- an industry-chain source that may become evidence after verification.

## When not to use

Do not use this workflow to:

- scrape X, batch collect social-media posts, or connect twscrape;
- call external data APIs;
- request, read, store, or infer cookies, API keys, sessions, or secrets;
- download or save large volumes of third-party original text;
- simulate Serenity's current view, private intent, portfolio, or endorsement;
- convert social-media heat, shortage narratives, or community excitement directly into confirmed 供应链卡点 evidence;
- generate real company investment conclusions, buy/sell instructions, position sizing, or return promises.

## Step 1: label source type

Assign one primary source label before analysis:

1. **Serenity original public expression**: short public wording attributed to Serenity and supplied with a locator.
2. **Community interpretation**: third-party commentary, summary, translation, or discussion.
3. **User-provided note**: user-authored summary, unsourced note, screenshot text, or private interpretation.
4. **Supply-chain evidence**: filing, company disclosure, transcript, industry data, or other auditable industry-chain material.
5. **Assistant inference**: the assistant's bounded hypothesis, uncertainty statement, or next-step recommendation.

If a user input contains multiple categories, split it into multiple Source Digests. Never relabel community interpretation as Serenity original public expression.

## Step 2: preserve attribution

Record the source title, URL or locator, source date, collection date, and provider. If the locator is missing, mark it as `unavailable` or `unknown` rather than filling in unverifiable detail. Do not store secrets, private locators, cookie strings, API keys, sessions, or private research material.

## Step 3: separate excerpt, paraphrase, translation, and interpretation

Keep four layers distinct:

- **Original excerpt**: the short supplied text, quoted only as much as needed for auditability.
- **Paraphrase**: a neutral restatement that does not strengthen the source.
- **Translation**: clearly labeled by source language, target language, and whether it is literal or paraphrased.
- **Interpretation**: any community reading, user reading, or assistant inference.

This separation prevents translated or summarized language from being mistaken for Serenity's original wording or for primary supply-chain evidence.

## Step 4: extract claim without overstating it

Extract the narrowest auditable claim. Prefer verbs such as `states`, `reports`, `suggests`, `claims`, or `indicates`. Avoid converting:

- management commentary into independently verified demand;
- backlog into durable chokepoint power;
- shortage narrative into confirmed 供应链卡点;
- community excitement into supply-chain evidence;
- Serenity public expression into official endorsement of this project or any company.

## Step 5: connect to evidence table only as hypothesis input

A Source Digest can feed an evidence table only as a hypothesis input. It should not decide the conclusion by itself. When mapping to an evidence table, record whether the source may support, contradict, or leave unresolved a candidate claim, and preserve the evidence level and confidence.

Social-media heat is not supply-chain chokepoint evidence. It may identify what to investigate next, but it must be checked against supply-chain mechanisms such as bottleneck process steps, throughput constraints, customer validation, capacity expansion lead time, substitution risk, pricing power, regulation, and counterevidence.

## Step 6: define missing checks

Every digest must include missing checks before it can influence 供应链卡点分析. Common checks include:

- primary-source verification;
- source date and context confirmation;
- capacity, yield, lead time, and qualification data;
- customer, supplier, competitor, and substitute evidence;
- geography and product-scope boundaries;
- counterevidence and negative cases;
- risks, tracking indicators, and invalidation conditions.

## Step 7: decide whether it can enter chokepoint research

A digest can enter chokepoint research only when it has clear provenance, a bounded claim, and explicit missing checks. Even then, it remains an input to an evidence chain, not an investment conclusion. If attribution is weak, source type is ambiguous, or the user requests advice or impersonation, keep the output at the workflow or refusal level.

## Quotation boundary

Use short quotations only when needed to preserve wording. Prefer paraphrase when possible. Do not retain long third-party original content, build bulk archives, or reproduce large source passages. If the user provides too much original text, ask them to narrow it or summarize it, and digest only a short excerpt.

## Community interpretation boundary

Community interpretation can help generate research hypotheses, but it cannot independently prove Serenity's view or a supply-chain chokepoint. It must be labeled as community interpretation and checked against original sources and supply-chain evidence before further use.

## Serenity impersonation / endorsement boundary

Do not simulate Serenity, write as Serenity, infer Serenity's current private view, or imply that Serenity has authorized, reviewed, endorsed, or approved this project. A Source Digest may describe a short Serenity original public expression when supplied by the user, but it must not transform that expression into an official statement about this repository, an industry conclusion, or a trade.

## Non-investment-advice boundary

Source Digest outputs are research workflow artifacts. They must not contain investment advice, buy/sell/hold instructions, position sizing, personalized recommendations, return promises, or real company conclusions. The allowed output is a labeled source摘要卡 plus missing checks for later evidence-chain review.