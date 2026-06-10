#!/usr/bin/env python3
"""Offline structural and content validation for serenity-chokepoint-skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


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
    "agents/serenity-chokepoint-researcher.md",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "docs/project-spec.md",
    "docs/distillation-rules.md",
    "docs/development-workflow.md",
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


class Validator:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.passes: list[str] = []

    def check(self, condition: bool, label: str, detail: str = "") -> None:
        if condition:
            self.passes.append(label)
            print(f"[PASS] {label}")
            return
        message = f"{label}: {detail}" if detail else label
        self.failures.append(message)
        print(f"[FAIL] {message}")


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def validate_files(validator: Validator) -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    validator.check(not missing, "required file structure", ", ".join(missing))


def validate_skill_entry(validator: Validator) -> None:
    text = read_text("SKILL.md")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    validator.check(frontmatter is not None, "SKILL.md YAML frontmatter")
    if frontmatter:
        metadata = frontmatter.group(1)
        validator.check(
            re.search(r"^name:\s*serenity-chokepoint-skill\s*$", metadata, re.MULTILINE)
            is not None,
            "SKILL.md name",
        )
        validator.check(
            re.search(r"^description:\s*\S.+$", metadata, re.MULTILINE) is not None,
            "SKILL.md description",
        )

    for heading in ["Purpose", "Terminology Guard", "Core Workflow", "Output Format"]:
        validator.check(f"# {heading}" in text, f"SKILL.md heading: {heading}")

    validator.check(CORE_SENTENCE in text, "SKILL.md frozen core sentence")
    validator.check(
        all(term in text for term in ["供应链卡点", "卡点理论", "供应链卡点分析"]),
        "SKILL.md default terminology",
    )
    validator.check(
        "research hypothesis" in text.lower() and "not investment advice" in text.lower(),
        "SKILL.md research-hypothesis boundary",
    )


def validate_readmes_and_policy(validator: Validator) -> None:
    readme_zh = read_text("README.zh-CN.md")
    project_spec = read_text("docs/project-spec.md")
    translation = read_text("references/translation-policy.md")

    validator.check(CORE_SENTENCE in readme_zh, "README.zh-CN.md frozen core sentence")
    validator.check(CORE_SENTENCE in project_spec, "project-spec frozen core sentence")
    validator.check(
        all(term in readme_zh for term in ["供应链卡点", "卡点理论", "供应链卡点分析"]),
        "README.zh-CN.md default terminology",
    )
    validator.check(
        "不构成投资建议" in readme_zh and "研究假设" in readme_zh,
        "README.zh-CN.md output boundary",
    )
    validator.check(
        "不默认译" in translation and "TOC / 制约理论" in translation,
        "translation policy boundary",
    )


def validate_prompt_pack(validator: Validator) -> None:
    prompt_pack = read_text("assets/research-prompt-pack.md")
    validator.check(
        len(re.findall(r"^## \d+\.", prompt_pack, re.MULTILINE)) >= 5,
        "Prompt Pack contains five prompts",
    )
    for phrase in ["证据链", "风险清单", "跟踪指标", "假设失效条件", "免责声明"]:
        validator.check(phrase in prompt_pack, f"Prompt Pack requires {phrase}")


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
    scores_valid = all(
        isinstance(item, dict)
        and isinstance(item.get("score"), int)
        and 0 <= item["score"] <= 5
        and bool(item.get("description"))
        for item in dimensions.values()
    )
    validator.check(scores_valid, "scorecard values and descriptions")


def validate_prohibited_language(validator: Validator) -> None:
    prohibited = [
        "Chokepoint Theory " + "就是 TOC",
        "必" + "买",
        "一定" + "上涨",
        "保证" + "收益",
        "个性化" + "投资建议",
    ]
    positive_equivalence = re.compile(
        r"Chokepoint Theory\s*(?:就是|等同于|=|is)\s*(?:TOC|制约理论|Theory of Constraints)",
        re.IGNORECASE,
    )
    violations: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".json"}:
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        for phrase in prohibited:
            if phrase in text:
                violations.append(f"{relative}: prohibited phrase")
        if positive_equivalence.search(text):
            violations.append(f"{relative}: direct Chokepoint/TOC equivalence")

    validator.check(not violations, "high-risk language scan", "; ".join(violations))


def main() -> int:
    validator = Validator()
    validate_files(validator)
    if validator.failures:
        print("\nValidation stopped because required files are missing.")
        return 1

    validate_skill_entry(validator)
    validate_readmes_and_policy(validator)
    validate_prompt_pack(validator)
    validate_scorecard(validator)
    validate_prohibited_language(validator)

    print(f"\nSummary: {len(validator.passes)} passed, {len(validator.failures)} failed.")
    if validator.failures:
        for failure in validator.failures:
            print(f"- {failure}")
        return 1

    print("serenity-chokepoint-skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
