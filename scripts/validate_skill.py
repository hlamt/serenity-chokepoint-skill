#!/usr/bin/env python3
"""Offline structural and consistency validation for serenity-chokepoint-skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

CORE_SENTENCE = (
    "Skill 引入 TOC / 制约理论作为系统性校准框架，帮助投研用户区分真正的供应链卡点、"
    "短期短缺、热门叙事与普通“卡脖子”概念，并避免将 Chokepoint Theory 简化误读为 TOC "
    "意义上的“瓶颈理论”。"
)

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "AGENTS.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "DISCLAIMER.md",
    "references/concept-boundary.md",
    "references/toc-comparison.md",
    "references/translation-policy.md",
    "references/serenity-chokepoint-patterns.md",
    "references/evidence-ladder.md",
    "references/market-source-playbook.md",
    "references/risk-and-compliance.md",
    "references/evidence-table.md",
    "references/framework-v0.1.md",
    "references/source-types.md",
    "references/serenity-source-policy.md",
    "assets/chokepoint-scorecard.json",
    "assets/research-prompt-pack.md",
    "assets/thesis-template.md",
    "assets/evidence-table-template.md",
    "assets/toc-boundary-checklist.md",
    "scripts/validate_skill.py",
    "scripts/chokepoint_scorecard.py",
    "examples/a-share-semiconductor-example.md",
    "examples/ai-infrastructure-chokepoint-example.md",
    "examples/toc-boundary-example.md",
    "examples/demo-conversation.md",
    "evals/boundary-checks.md",
    "evals/test-cases.md",
    "evals/anti-patterns.md",
    "evals/source-boundary-test-cases.md",
    "agents/serenity-chokepoint-researcher.md",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "docs/project-spec.md",
    "docs/source-evidence-plan.md",
    "docs/distillation-rules.md",
    "docs/development-workflow.md",
]

SKILL_HEADINGS = [
    "Purpose",
    "When to Use",
    "When Not to Use",
    "Terminology Guard",
    "Core Workflow",
    "Output Format",
    "Evidence Requirements",
    "Boundary Rules",
    "Risk and Disclaimer",
    "References",
]

OUTPUT_SECTIONS = [
    "研究问题",
    "产业价值链",
    "有效产出定义",
    "候选供应链卡点",
    "候选公司",
    "证据链",
    "反证与风险",
    "跟踪指标",
    "假设失效条件",
    "免责声明",
]

OUTPUT_CONTRACT_FILES = [
    "SKILL.md",
    "assets/thesis-template.md",
    "examples/a-share-semiconductor-example.md",
    "examples/ai-infrastructure-chokepoint-example.md",
    "examples/demo-conversation.md",
]

EVIDENCE_SCHEMA = [
    "evidence_id",
    "claim",
    "source_type",
    "source_title",
    "source_url",
    "date",
    "evidence_level",
    "supports",
    "contradicts",
    "confidence",
    "notes",
]

EVIDENCE_SCHEMA_FILES = [
    "references/evidence-table.md",
    "assets/evidence-table-template.md",
    "assets/thesis-template.md",
    "examples/a-share-semiconductor-example.md",
    "examples/ai-infrastructure-chokepoint-example.md",
    "examples/demo-conversation.md",
    "examples/toc-boundary-example.md",
]

SCORECARD_FIELDS = [
    "demand_pressure",
    "throughput_impact",
    "ccr_characteristics",
    "substitution_difficulty",
    "elevation_lead_time",
    "subordination_evidence",
    "economic_capture",
    "mispricing_potential",
    "migration_risk",
    "evidence_quality",
]

PROMPT_REQUIRED_TERMS = [
    "候选供应链卡点",
    "候选公司",
    "证据链",
    "风险清单",
    "跟踪指标",
    "假设失效条件",
    "免责声明",
]

SOURCE_EVIDENCE_TEXT_FILES = [
    "docs/source-evidence-plan.md",
    "references/source-types.md",
    "references/serenity-source-policy.md",
    "evals/source-boundary-test-cases.md",
]

SOURCE_POLICY_TERMS = [
    "public expression",
    "attribution",
    "paraphrase",
    "quotation",
    "endorsement",
    "impersonate",
    "investment advice",
]

SOURCE_BOUNDARY_TEST_TERMS = [
    "batch scrape",
    "community interpretation",
    "official endorsement",
    "buy/sell",
    "company disclosure",
]

PUBLIC_PLACEHOLDERS = [
    ("<your-org>", re.compile(r"<your-org>", re.IGNORECASE)),
    ("example.invalid", re.compile(r"example\.invalid", re.IGNORECASE)),
    ("TODO", re.compile(r"\bTODO\b", re.IGNORECASE)),
    ("TBD", re.compile(r"\bTBD\b", re.IGNORECASE)),
]

ALLOWED_PLACEHOLDERS = {(path, "TBD") for path in EVIDENCE_SCHEMA_FILES}


class Validator:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def check(self, condition: bool, label: str, detail: str = "") -> None:
        if condition:
            self.passes.append(label)
            print(f"[PASS] {label}")
            return
        message = f"{label}: {detail}" if detail else label
        self.failures.append(message)
        print(f"[FAIL] {message}")

    def warn(self, label: str, detail: str) -> None:
        message = f"{label}: {detail}"
        self.warnings.append(message)
        print(f"[WARN] {message}")


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def repository_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.relative_to(ROOT).parts
        and "__pycache__" not in path.relative_to(ROOT).parts
    )


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "opening delimiter is missing"
    try:
        closing_index = next(
            index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"
        )
    except StopIteration:
        return {}, "closing delimiter is missing"

    metadata: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return {}, f"invalid metadata line {line_number}"
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"\'')
        if not key or not value:
            return {}, f"empty key or value on metadata line {line_number}"
        if key in metadata:
            return {}, f"duplicate metadata key: {key}"
        metadata[key] = value
    return metadata, None


def markdown_table_header(text: str) -> list[str] | None:
    for line in text.splitlines():
        if not line.lstrip().startswith("| evidence_id |"):
            continue
        return [cell.strip() for cell in line.strip().strip("|").split("|")]
    return None


def validate_files(validator: Validator) -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    validator.check(not missing, "required file structure", ", ".join(missing))


def validate_utf8_and_nonempty(validator: Validator) -> None:
    empty: list[str] = []
    invalid_utf8: list[str] = []
    for path in repository_files():
        relative = path.relative_to(ROOT)
        if path.name == ".gitkeep":
            continue
        data = path.read_bytes()
        if not data:
            empty.append(str(relative))
            continue
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            invalid_utf8.append(str(relative))
    validator.check(not empty, "non-.gitkeep files are nonempty", ", ".join(empty))
    validator.check(not invalid_utf8, "repository text is UTF-8", ", ".join(invalid_utf8))


def validate_source_evidence_files(validator: Validator) -> None:
    unreadable: list[str] = []
    empty: list[str] = []
    for relative_path in SOURCE_EVIDENCE_TEXT_FILES:
        try:
            text = read_text(relative_path)
        except UnicodeDecodeError:
            unreadable.append(relative_path)
            continue
        if not text.strip():
            empty.append(relative_path)

    validator.check(not unreadable, "source evidence text files are UTF-8", ", ".join(unreadable))
    validator.check(not empty, "source evidence text files are nonempty", ", ".join(empty))

    if unreadable or empty:
        return

    source_policy = read_text("references/serenity-source-policy.md")
    missing_policy_terms = [term for term in SOURCE_POLICY_TERMS if term not in source_policy]
    validator.check(
        not missing_policy_terms,
        "serenity source policy required terms",
        ", ".join(missing_policy_terms),
    )

    boundary_tests = read_text("evals/source-boundary-test-cases.md")
    missing_boundary_terms = [
        term for term in SOURCE_BOUNDARY_TEST_TERMS if term not in boundary_tests
    ]
    validator.check(
        not missing_boundary_terms,
        "source boundary test required terms",
        ", ".join(missing_boundary_terms),
    )


def validate_skill_entry(validator: Validator) -> None:
    text = read_text("SKILL.md")
    metadata, error = parse_frontmatter(text)
    validator.check(error is None, "SKILL.md YAML frontmatter", error or "")
    if error is None:
        for key in ["name", "description", "version"]:
            validator.check(bool(metadata.get(key)), f"SKILL.md metadata: {key}")
        validator.check(
            metadata.get("name") == "serenity-chokepoint-skill",
            "SKILL.md canonical name",
            metadata.get("name", "missing"),
        )

    for heading in SKILL_HEADINGS:
        found = re.search(rf"^# {re.escape(heading)}\s*$", text, re.MULTILINE) is not None
        validator.check(found, f"SKILL.md H1: {heading}")

    validator.check(CORE_SENTENCE in text, "SKILL.md frozen core sentence")
    validator.check(
        all(term in text for term in ["供应链卡点", "卡点理论", "供应链卡点分析"]),
        "SKILL.md default terminology",
    )
    validator.check(
        "research hypothesis" in text.lower() and "not investment advice" in text.lower(),
        "SKILL.md research-hypothesis boundary",
    )


def contract_term_present(text: str, term: str) -> bool:
    pattern = rf"^(?:#{{1,6}}\s+(?:\d+\.\s*)?|\d+\.\s*){re.escape(term)}\s*$"
    return re.search(pattern, text, re.MULTILINE) is not None


def validate_output_contract(validator: Validator) -> None:
    for relative_path in OUTPUT_CONTRACT_FILES:
        text = read_text(relative_path)
        missing = [term for term in OUTPUT_SECTIONS if not contract_term_present(text, term)]
        validator.check(
            not missing,
            f"ten-section output contract: {relative_path}",
            ", ".join(missing),
        )


def validate_readmes_and_policy(validator: Validator) -> None:
    readme_zh = read_text("README.zh-CN.md")
    readme_en = read_text("README.en.md")
    project_spec = read_text("docs/project-spec.md")
    translation = read_text("references/translation-policy.md")

    validator.check(CORE_SENTENCE in readme_zh, "README.zh-CN.md frozen core sentence")
    validator.check(CORE_SENTENCE in project_spec, "project-spec frozen core sentence")
    validator.check(
        all(term in readme_zh for term in OUTPUT_SECTIONS),
        "README.zh-CN.md ten-section vocabulary",
    )
    english_sections = [
        "Research question",
        "Value chain",
        "Throughput definition",
        "Candidate supply-chain chokepoints",
        "Candidate companies",
        "Evidence chain",
        "Counterevidence and risks",
        "Tracking indicators",
        "Invalidation conditions",
        "Disclaimer",
    ]
    validator.check(
        all(term in readme_en for term in english_sections),
        "README.en.md ten-section vocabulary",
    )
    validator.check(
        "https://github.com/hlamt/serenity-chokepoint-skill" in readme_zh
        and "https://github.com/hlamt/serenity-chokepoint-skill" in readme_en,
        "canonical repository URL",
    )
    validator.check(
        "不构成投资建议" in readme_zh and "研究假设" in readme_zh,
        "README.zh-CN.md output boundary",
    )
    validator.check(
        "不默认译" in translation and "TOC / 制约理论" in translation,
        "translation policy boundary",
    )


def validate_evidence_schema(validator: Validator) -> None:
    for relative_path in EVIDENCE_SCHEMA_FILES:
        header = markdown_table_header(read_text(relative_path))
        validator.check(
            header == EVIDENCE_SCHEMA,
            f"evidence schema: {relative_path}",
            f"expected {EVIDENCE_SCHEMA}, got {header}",
        )


def prompt_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^## (\d+)\.\s+(.+)$", text, re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1), text[match.start():end]))
    return sections


def validate_prompt_pack(validator: Validator) -> None:
    sections = prompt_sections(read_text("assets/research-prompt-pack.md"))
    validator.check(len(sections) == 5, "Prompt Pack contains exactly five prompts")
    for number, section in sections:
        missing_required = [term for term in PROMPT_REQUIRED_TERMS if term not in section]
        missing_contract = [term for term in OUTPUT_SECTIONS if term not in section]
        validator.check(
            not missing_required,
            f"Prompt {number} required research fields",
            ", ".join(missing_required),
        )
        validator.check(
            not missing_contract,
            f"Prompt {number} ten-section contract",
            ", ".join(missing_contract),
        )


def validate_scorecard(validator: Validator) -> None:
    try:
        data = json.loads(read_text("assets/chokepoint-scorecard.json"))
    except (OSError, json.JSONDecodeError) as exc:
        validator.check(False, "scorecard JSON parses", str(exc))
        return

    validator.check(True, "scorecard JSON parses")
    dimensions = data.get("dimensions", {})
    validator.check(
        list(dimensions) == SCORECARD_FIELDS,
        "scorecard dimensions",
        "expected the ten dimensions in the documented order",
    )

    invalid: list[str] = []
    for name, item in dimensions.items():
        if not isinstance(item, dict):
            invalid.append(f"{name}: not an object")
            continue
        if item.get("name") != name:
            invalid.append(f"{name}: name mismatch")
        if not isinstance(item.get("description"), str) or not item["description"].strip():
            invalid.append(f"{name}: description missing")
        if item.get("score_range") != [0, 5]:
            invalid.append(f"{name}: score_range must be [0, 5]")
        if item.get("polarity") not in {"positive", "negative"}:
            invalid.append(f"{name}: invalid polarity")
        score = item.get("score")
        if not isinstance(score, int) or not 0 <= score <= 5:
            invalid.append(f"{name}: score must be an integer from 0 to 5")
    validator.check(not invalid, "scorecard dimension schema", "; ".join(invalid))
    validator.check(
        dimensions.get("migration_risk", {}).get("polarity") == "negative",
        "migration_risk negative polarity",
    )
    positive_mismatch = [
        name
        for name in SCORECARD_FIELDS
        if name != "migration_risk"
        and dimensions.get(name, {}).get("polarity") != "positive"
    ]
    validator.check(
        not positive_mismatch,
        "positive scorecard polarity",
        ", ".join(positive_mismatch),
    )


def validate_markdown_links(validator: Validator) -> None:
    missing: list[str] = []
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in repository_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for match in link_pattern.finditer(text):
            raw_target = match.group(1).strip()
            if raw_target.startswith("<") and ">" in raw_target:
                target = raw_target[1:raw_target.index(">")]
            else:
                target = raw_target.split(maxsplit=1)[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            destination = (path.parent / target).resolve()
            if not destination.exists():
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
    validator.check(not missing, "Markdown relative links", "; ".join(missing))


def validate_public_placeholders(validator: Validator) -> None:
    findings: list[str] = []
    for path in repository_files():
        if path.suffix.lower() not in {".md", ".json"}:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in PUBLIC_PLACEHOLDERS:
            relative = str(path.relative_to(ROOT))
            if pattern.search(text) and (relative, label) not in ALLOWED_PLACEHOLDERS:
                findings.append(f"{relative}: {label}")
    if findings:
        validator.warn("public placeholder scan", "; ".join(findings))
    else:
        validator.passes.append("public placeholder scan")
        print("[PASS] public placeholder scan")


def has_negative_context(context: str, match_start_in_line: int, line: str) -> bool:
    prefix = line[max(0, match_start_in_line - 32):match_start_in_line]
    local_context = f"{context}\n{prefix}".lower()
    negative_markers = [
        "不",
        "非",
        "无",
        "禁止",
        "避免",
        "不得",
        "不可",
        "拒绝",
        "错误表达",
        "反模式",
        "do not",
        "does not",
        "is not",
        "must not",
        "never",
        "avoid",
        "anti-pattern",
    ]
    return any(marker in local_context for marker in negative_markers)


def validate_high_risk_language(validator: Validator) -> None:
    risky_patterns = [
        ("必买", re.compile(r"必买")),
        ("一定上涨", re.compile(r"一定上涨")),
        ("保证收益", re.compile(r"保证收益")),
        (
            "direct Chokepoint/TOC equivalence",
            re.compile(
                r"Chokepoint Theory\s*(?:就是|等同于|=|is)\s*(?:TOC|制约理论|Theory of Constraints)",
                re.IGNORECASE,
            ),
        ),
    ]
    violations: list[str] = []
    for path in repository_files():
        if path.suffix.lower() not in {".md", ".json"}:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_number, line in enumerate(lines, start=1):
            preceding_context = "\n".join(lines[max(0, line_number - 3):line_number - 1])
            for label, pattern in risky_patterns:
                for match in pattern.finditer(line):
                    if has_negative_context(preceding_context, match.start(), line):
                        continue
                    violations.append(f"{path.relative_to(ROOT)}:{line_number}: {label}")
    validator.check(not violations, "affirmative high-risk language scan", "; ".join(violations))


def main() -> int:
    validator = Validator()
    validate_files(validator)
    if validator.failures:
        print("\nValidation stopped because required files are missing.")
        return 1

    validate_utf8_and_nonempty(validator)
    validate_source_evidence_files(validator)
    validate_skill_entry(validator)
    validate_output_contract(validator)
    validate_readmes_and_policy(validator)
    validate_evidence_schema(validator)
    validate_prompt_pack(validator)
    validate_scorecard(validator)
    validate_markdown_links(validator)
    validate_public_placeholders(validator)
    validate_high_risk_language(validator)

    print(
        f"\nSummary: {len(validator.passes)} passed, "
        f"{len(validator.warnings)} warnings, {len(validator.failures)} failed."
    )
    if validator.failures:
        for failure in validator.failures:
            print(f"- {failure}")
        return 1

    print("serenity-chokepoint-skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
