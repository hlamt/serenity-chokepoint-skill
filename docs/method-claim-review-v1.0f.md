# Method Claim Review — V1.0F

## 1. Purpose and review boundary

This file reviews the six method claim candidates in `docs/method-claim-candidates-v1.0e.md`. It records bounded dispositions, safer wording, evidence gaps, and questions for later review.

- This is not validated method claims.
- This is not TOC calibration.
- This is not final Chokepoint Theory distillation.
- This is not a Skill runtime file.
- This is not investment advice.

No disposition below promotes a candidate into the method layer or authorizes runtime use.

## 2. Review summary

| claim_id | current_status | recommended_disposition | recommended_wording_summary | runtime_readiness | next_evidence_needed |
| --- | --- | --- | --- | --- | --- |
| MCC-0001 | `candidate_not_validated` | `narrow_scope` | Map repeated entity participation across potentially constrained layers, but test every layer independently before inferring a system constraint. | `review_only` | Serenity original expressions, counterexamples, and cross-case evidence distinguishing repeated dependency from an active system constraint. |
| MCC-0002 | `candidate_not_validated` | `narrow_scope` | Use tracing toward physical inputs only to generate hypotheses; require separate scarcity, throughput, substitution, and boundary evidence. | `review_only` | Serenity original expressions plus cases involving nonphysical constraints, substitution, capacity, and false-positive upstream dependencies. |
| MCC-0003 | `candidate_not_validated` | `keep_as_candidate` | Test operating constraint, firm-level economic capture, and common-shareholder capture separately. | `review_only` | Serenity original expressions, cross-case capture evidence, and counterexamples where constraint evidence did not produce shareholder capture. |
| MCC-0004 | `insufficient_serenity_support` | `downgrade_to_source_governance_rule` | Treat financing and capacity announcements as dated evidence of a possible elevation action, not proof of constraint release. | `not_runtime_ready` | Serenity original support, completion and utilization evidence, and cases where announced capacity failed to change throughput or economics. |
| MCC-0005 | `insufficient_serenity_support` | `downgrade_to_source_governance_rule` | Preserve source roles and require claim-appropriate corroboration; do not let one source establish a broad company-level chokepoint conclusion. | `not_runtime_ready` | Serenity original source-practice expressions, cross-case corroboration tests, and counterevidence on source-role failures. |
| MCC-0006 | `insufficient_serenity_support` | `exclude_from_method_layer` | Do not reconstruct unavailable text; only reviewable, provenance-preserving records may enter a support chain. | `not_runtime_ready` | Governance review and provenance failure cases; no method-layer evidence target is currently justified. |

## 3. Individual review notes

### MCC-0001

```yaml
claim_id: MCC-0001
original_claim_text: "A candidate chokepoint review should test whether the same entity appears at more than one constrained layer rather than assuming that one claimed bottleneck is the whole system constraint."
review_disposition: narrow_scope
recommended_wording: "In a candidate case, map whether one entity participates at multiple potentially constrained layers, then test each layer independently before inferring a system constraint."
source_support_review:
  serenity_original_expression: "Partial support from SRC-0001 only; it is a single provisionally approved public expression candidate and does not establish a general rule."
  industry_evidence: "No independent industry evidence currently supports this as a general method claim."
  company_evidence: "No company evidence currently tests whether repeated entity participation identifies, or fails to identify, the system constraint."
  secondary_evidence: "No secondary evidence currently provides cross-case corroboration."
  provenance_or_governance: "SRC-0001 has explicit limitations and remains a seed source record not distilled."
reasoning: "The candidate preserves a useful mapping question, but its original wording risks collapsing repeated participation, local bottlenecks, and the whole-system constraint into one inference. The narrower wording makes the mapping hypothesis-generating and requires layer-by-layer testing."
risk_if_promoted_too_early: "A recurring company or asset could be labeled the system constraint merely because it appears in several dependency maps, producing circular case selection and overgeneralization from one public expression."
required_next_evidence:
  - "Targeted Serenity X original expressions that explicitly map, reject, or qualify one entity appearing across multiple constrained layers."
  - "Reviewable Serenity Reddit original expressions beyond the current single candidate."
  - "Cross-case examples where repeated entity participation did and did not correspond to an active system constraint."
  - "Counterevidence distinguishing common dependency, local bottleneck, and whole-system constraint."
toc_calibration_question: "Under TOC, what additional tests are required before repeated participation across layers can be treated as evidence about the system constraint rather than a dependency map?"
runtime_readiness: review_only
reviewer_note: "Retain only as a narrowed review candidate. Do not convert the repeated-layer observation into a company or investment conclusion."
```

### MCC-0002

```yaml
claim_id: MCC-0002
original_claim_text: "A candidate research sequence may trace demand downward through the value chain until it reaches physical materials, capacity, or other hard supply floors, while separately testing whether each mapped layer is actually constraining."
review_disposition: narrow_scope
recommended_wording: "Trace demand toward physical inputs as one hypothesis-generating step, but treat a physical dependency as a constraint only after evidence of scarcity, throughput impact, substitution difficulty, and system boundary."
source_support_review:
  serenity_original_expression: "Partial support from SRC-0001 only; the record suggests upstream tracing in one candidate case but does not validate a general stopping rule."
  industry_evidence: "SRC-0002 corroborates bounded indium supply context, but it cannot establish that tracing to a physical input identifies the operative constraint in general or in a specific company case."
  company_evidence: "Current company records do not establish non-bypassability, active throughput limitation, or the relevant system boundary."
  secondary_evidence: "No secondary source supplies a general cross-case test."
  provenance_or_governance: "The available records preserve source roles, but the evidence chain remains incomplete and not distilled."
reasoning: "Backward tracing can expose candidate dependencies, yet physicality alone does not establish a constraint. The review wording adds scarcity, throughput, substitution, and boundary tests and avoids assuming that every important constraint is physical."
risk_if_promoted_too_early: "The method could systematically overselect upstream materials, mistake dependency for constraint, ignore policy, qualification, demand, or organizational constraints, and produce unsupported company conclusions."
required_next_evidence:
  - "Targeted Serenity X original expressions describing when backward tracing should stop and what makes a dependency non-bypassable."
  - "Reviewable Serenity Reddit original expressions on physical versus nonphysical constraints."
  - "Industry evidence on capacity, substitution, qualification, recycling, inventories, and lead times."
  - "Cross-case and counterevidence where an upstream physical dependency was important but was not the active system constraint."
toc_calibration_question: "How should backward supply-chain tracing be reconciled with TOC's requirement to identify the constraint of a defined system, including constraints that are not physical inputs?"
runtime_readiness: review_only
reviewer_note: "Keep the tracing step only as hypothesis generation. No current source set supports a universal physical-dependency rule."
```

### MCC-0003

```yaml
claim_id: MCC-0003
original_claim_text: "Identifying a supply-chain constraint is not sufficient to infer common-shareholder value capture; financing, dilution, entity structure, operating conversion, and market expectations require separate review."
review_disposition: keep_as_candidate
recommended_wording: "After proposing a supply-chain constraint, separately test the operating constraint, firm-level economic capture, and common-shareholder capture; evidence for one does not establish the others."
source_support_review:
  serenity_original_expression: "SRC-0001 offers limited support for examining a candidate operating dependency, but it does not fully articulate the three-layer separation."
  industry_evidence: "SRC-0002 can inform industry context only; it does not establish firm-level or shareholder capture."
  company_evidence: "SRC-0003 provides bounded financing evidence relevant to dilution and funding, but it does not prove constraint ownership, economic capture, or shareholder benefit."
  secondary_evidence: "SRC-0005, where used, is secondary-only context and cannot independently establish any capture layer."
  provenance_or_governance: "The source-role separation in the seed records supports reviewing the layers independently, while all records remain undistilled."
reasoning: "This is the strongest candidate because it explicitly blocks a common inferential leap from an operating bottleneck to an investable security. It remains a candidate because the current corpus does not show that this wording is Serenity-derived, cross-case tested, or TOC-calibrated."
risk_if_promoted_too_early: "Users could treat a useful analytical boundary as already validated, or infer that identifying a chokepoint automatically identifies the firm, security, timing, or economics through which value will be captured."
required_next_evidence:
  - "Targeted Serenity X original expressions that explicitly distinguish operating constraint, firm economics, financing structure, and shareholder capture."
  - "Reviewable Serenity Reddit original expressions applying or qualifying that separation."
  - "Cross-case evidence where operating constraints produced different firm-level and shareholder outcomes."
  - "Counterexamples involving dilution, customer power, substitution, regulation, cyclicality, or failed capacity execution."
toc_calibration_question: "Which parts of this separation belong to TOC system analysis, and which are external investment-analysis overlays that must remain outside a TOC claim?"
runtime_readiness: review_only
reviewer_note: "Keep as a candidate for further evidence collection. It must not be presented as a validated method claim or as investment guidance."
```

### MCC-0004

```yaml
claim_id: MCC-0004
original_claim_text: "A financing purpose or capacity-expansion plan is only a candidate elevation path; it does not show that a constraint has been released or that new capacity is qualified, utilized, profitable, or value-accretive."
review_disposition: downgrade_to_source_governance_rule
recommended_wording: "Treat financing and capacity announcements as dated evidence of a possible elevation action, not evidence of constraint release; require completion, qualification, utilization, throughput, and economics evidence."
source_support_review:
  serenity_original_expression: "No Serenity original expression currently supports this as a method claim."
  industry_evidence: "No industry record in the current set demonstrates that a financing or capacity announcement elevated an active constraint."
  company_evidence: "SRC-0003 documents a specific financing event. It can verify the event and stated use of proceeds, but not completion, operational effect, constraint release, or economic capture."
  secondary_evidence: "SRC-0005 may contextualize the offering only as a secondary source and does not validate the proposed rule."
  provenance_or_governance: "The available support is event evidence with explicit date and source-role boundaries, making the candidate better suited to evidence-handling guidance."
reasoning: "The current corpus supports recording what a company announced or financed, not interpreting the event as a TOC elevation action. A governance rule can prevent announcements from being promoted into operational conclusions while preserving them as dated evidence."
risk_if_promoted_too_early: "Capital raising or planned capacity could be mistaken for completed capacity, qualified output, additional throughput, constraint relief, or shareholder value creation."
required_next_evidence:
  - "Targeted Serenity X or Reddit original expressions linking financing or capacity action to constraint elevation with explicit qualifications."
  - "Company evidence for project completion, qualification, utilization, yields, throughput, and unit economics."
  - "Cross-case evidence comparing announced, completed, and effective elevation actions."
  - "Counterevidence where financing or capacity expansion failed, arrived late, moved the constraint, or impaired shareholder capture."
toc_calibration_question: "What observable evidence is required under TOC to distinguish an announced elevation attempt from successful elevation, exploitation, or movement of the constraint?"
runtime_readiness: not_runtime_ready
reviewer_note: "Downgrade to a source-governance rule. The current evidence supports disciplined event labeling, not a Serenity-derived or TOC-calibrated method claim."
```

### MCC-0005

```yaml
claim_id: MCC-0005
original_claim_text: "No single industry, company, or secondary source should independently establish a company-level chokepoint conclusion; source roles, periods, definitions, and primary-versus-secondary status must remain separated."
review_disposition: downgrade_to_source_governance_rule
recommended_wording: "Preserve source roles and require claim-appropriate corroboration; a single industry, company, or secondary source may verify a narrow fact but cannot alone establish a company-level chokepoint conclusion."
source_support_review:
  serenity_original_expression: "No Serenity original expression currently establishes this as part of Chokepoint Theory."
  industry_evidence: "SRC-0002 can support bounded industry facts within its scope, but it cannot establish a company-level chokepoint conclusion."
  company_evidence: "SRC-0003 and SRC-0004 can support bounded company facts within their scopes, but issuer evidence alone cannot validate the broader conclusion."
  secondary_evidence: "SRC-0005 is explicitly secondary-only and must not carry a company-level conclusion by itself."
  provenance_or_governance: "The source records' allowed-use and disallowed-use fields directly support this as corpus governance rather than a substantive method claim."
reasoning: "Claim-appropriate corroboration is a defensible review control, but an absolute multi-source rule would be too crude because one authoritative source may establish a narrow fact. The revised wording protects source roles and scales corroboration to the breadth of the proposed conclusion."
risk_if_promoted_too_early: "A procedural safeguard could be mislabeled as validated Chokepoint Theory, while mechanical source counting could either overstate weak corroboration or discount a definitive source for a narrow fact."
required_next_evidence:
  - "Targeted Serenity original expressions about corroboration, source hierarchy, and promotion from hypothesis to conclusion."
  - "Cross-case tests of which source combinations were sufficient or insufficient for different claim types."
  - "Counterevidence involving circular reporting, issuer bias, stale data, conflicting authoritative sources, and false corroboration."
  - "A reviewed claim-to-source-role matrix before any runtime implementation."
toc_calibration_question: "Is corroboration part of TOC reasoning itself, or an epistemic and provenance control that should remain outside TOC calibration?"
runtime_readiness: not_runtime_ready
reviewer_note: "Downgrade to source governance. This rule may govern future review packets, but it is not a validated method claim and is not runtime-ready."
```

### MCC-0006

```yaml
claim_id: MCC-0006
original_claim_text: "Deleted or unavailable post bodies should not be reconstructed or used in a method-support chain; only separately reviewable surviving records may contribute support."
review_disposition: exclude_from_method_layer
recommended_wording: "Do not reconstruct unavailable source text; only reviewable, provenance-preserving records may enter a support chain."
source_support_review:
  serenity_original_expression: "No Serenity original expression currently supports this as a substantive Chokepoint Theory claim."
  industry_evidence: "No industry evidence is needed to establish the immediate provenance boundary."
  company_evidence: "SRC-0004 demonstrates a bounded provenance limitation: reviewable issuer material can be recorded while inaccessible or unavailable material is not reconstructed."
  secondary_evidence: "Secondary sources cannot restore missing original text or substitute for an unavailable primary expression without explicit attribution and scope limits."
  provenance_or_governance: "Strong governance relevance. The rule follows the corpus boundary against reconstructing deleted Reddit post bodies and preserves auditability."
reasoning: "The candidate is an evidence-integrity rule, not a claim about how constraints operate. Keeping it outside the method layer prevents provenance controls from being mistaken for Chokepoint Theory content."
risk_if_promoted_too_early: "A necessary corpus safeguard could inflate the apparent method corpus, blur theory with evidence hygiene, and create a false impression that the rule was distilled from Serenity."
required_next_evidence:
  - "Governance review of provenance failure cases, unavailable originals, quotations, paraphrases, and surviving comments."
  - "A future corpus policy decision on whether this rule belongs in acquisition, review, or distillation controls."
  - "No method-layer evidence collection unless later review identifies a distinct substantive claim."
toc_calibration_question: "None identified. Keep this provenance rule outside TOC calibration unless a later substantive method claim is separately proposed."
runtime_readiness: not_runtime_ready
reviewer_note: "Exclude from the method layer while retaining the boundary as source governance. Deleted or unavailable text must not be reconstructed."
```

## 4. Consolidated source gap list

### 4.1 Serenity X original expression gaps

- Targeted original expressions for repeated entities across constrained layers.
- Targeted original expressions defining when backward tracing reaches a meaningful constraint candidate.
- Targeted original expressions separating operating constraint, firm-level economics, and common-shareholder capture.
- Targeted original expressions, if any, on financing, capacity actions, corroboration, and evidentiary promotion.
- Explicit counterexamples, qualifications, retractions, or changes in Serenity's framing.

### 4.2 Reddit original expression gaps

- Reviewable original posts or comments that preserve author, date, permalink, and bounded text.
- Independent support beyond SRC-0001 for MCC-0001 through MCC-0003.
- No reconstruction of LEAD-003, LEAD-004, or any other deleted post body.
- Surviving comment permalinks must be reviewed as separate units rather than used to recreate a deleted top-level post.

### 4.3 Cross-case evidence gaps

- Cases where a repeated entity was and was not the active system constraint.
- Cases where backward physical tracing produced a useful candidate and cases where it produced a false positive.
- Cases separating operating constraint, firm capture, and shareholder capture.
- Cases comparing announced elevation actions with completed and effective outcomes.

### 4.4 Industry and company evidence gaps

- Capacity, substitution, qualification, recycling, inventory, lead-time, utilization, yield, and throughput evidence.
- Completion and operating evidence following financing or capacity announcements.
- Economic evidence separating issuer revenue opportunity from costs, bargaining power, dilution, and common-shareholder outcomes.
- Dated, filing-level evidence rather than company index pages or broad landing pages.

### 4.5 Counterevidence gaps

- Nonphysical constraints and constraints outside the initially selected system boundary.
- Substitution, demand destruction, excess capacity, technical failure, qualification delays, regulation, and customer concentration.
- Financing, dilution, execution, or timing outcomes that prevent firm or shareholder capture.
- Circular reporting, issuer bias, stale evidence, and superficially independent sources sharing the same origin.

### 4.6 TOC calibration gaps

- Defined system boundary, goal, throughput measure, and evidence of the active constraint.
- Distinctions among dependency, bottleneck, constraint, exploitation, subordination, elevation, and movement of the constraint.
- Tests for whether the candidate language is compatible with TOC without claiming that TOC calibration has been completed.
- Separation of TOC system analysis from external company, security, and investment-analysis overlays.

## 5. Required next step

The next prioritized work item should be:

**V1.0G — Targeted X Original Expression Gap Search**

That search must be limited to the specific Serenity original-expression gaps identified in this review. It must use bounded, reviewable public locators or user-provided materials and must not become generalized timeline scraping. It must not use `twscrape`, the X API, cookies, sessions, tokens, API keys, secrets, login-wall bypasses, or bulk capture. Any collected unit must retain provenance and remain a review input rather than a validated method claim.

This file is a review artifact only. It contains no validated method claims, no final Chokepoint Theory distillation, no TOC calibration conclusions, no real company conclusions, and no investment advice. No claim in this file is ready for Skill runtime use.
