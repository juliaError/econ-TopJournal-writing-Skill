#!/usr/bin/env python3
"""Audit main-text conservation between two LaTeX manuscripts.

This standard-library-only guardrail measures deterministic changes. It does
not decide whether prose is substantively sufficient; pair it with the
Main-Text Sufficiency and Conservation Role.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0"
EXIT_CODES = {
    "pass": 0,
    "fail": 1,
    "approval_required": 2,
    "metric_unavailable": 3,
}


class MetricUnavailable(RuntimeError):
    """Raised when a deterministic manuscript metric cannot be reproduced."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def strip_latex_comments(text: str) -> str:
    cleaned: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for index, character in enumerate(line):
            if character != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        fragment = line[:cut]
        if line.endswith("\n") and not fragment.endswith("\n"):
            fragment += "\n"
        cleaned.append(fragment)
    return "".join(cleaned)


INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^{}]+)\}")


def ensure_within_root(path: Path, root: Path) -> None:
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise MetricUnavailable(f"include escapes project root: {path}") from exc


def resolve_input(raw: str, current_file: Path, project_root: Path) -> Path:
    child = Path(raw.strip())
    if not child.suffix:
        child = child.with_suffix(".tex")
    if not child.is_absolute():
        child = current_file.parent / child
    child = child.resolve()
    ensure_within_root(child, project_root)
    if not child.is_file():
        raise MetricUnavailable(f"included file not found: {child}")
    return child


def expand_tex(
    path: Path,
    project_root: Path,
    stack: tuple[Path, ...] = (),
) -> tuple[str, list[str]]:
    path = path.resolve()
    ensure_within_root(path, project_root)
    if path in stack:
        cycle = " -> ".join(str(item) for item in (*stack, path))
        raise MetricUnavailable(f"cyclic LaTeX include: {cycle}")
    if not path.is_file():
        raise MetricUnavailable(f"manuscript file not found: {path}")
    try:
        text = strip_latex_comments(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError as exc:
        raise MetricUnavailable(f"file is not valid UTF-8: {path}") from exc

    output: list[str] = []
    sources = [str(path)]
    position = 0
    for match in INPUT_RE.finditer(text):
        output.append(text[position : match.start()])
        child = resolve_input(match.group(1), path, project_root)
        child_text, child_sources = expand_tex(child, project_root, (*stack, path))
        output.append(child_text)
        sources.extend(child_sources)
        position = match.end()
    output.append(text[position:])
    return "".join(output), sources


def marker_pattern(marker: str) -> re.Pattern[str]:
    suffix = r"(?![A-Za-z@])" if marker and marker[-1].isalpha() else ""
    return re.compile(re.escape(marker) + suffix)


def split_appendix(text: str, marker: str, label: str) -> tuple[str, str]:
    matches = list(marker_pattern(marker).finditer(text))
    if len(matches) != 1:
        raise MetricUnavailable(
            f"{label} requires exactly one appendix marker {marker!r}; found {len(matches)}"
        )
    match = matches[0]
    return text[: match.start()], text[match.end() :]


def raw_source_words(text: str) -> int:
    return len(re.findall(r"\S+", text))


DROP_ARGUMENT_COMMANDS = re.compile(
    r"\\(?:label|ref|eqref|autoref|pageref|cite\w*|url|href)\*?"
    r"(?:\s*\[[^\]]*\])*\s*\{[^{}]*\}"
)


def normalized_words(text: str) -> int:
    cleaned = DROP_ARGUMENT_COMMANDS.sub(" ", text)
    cleaned = re.sub(r"\$\$.*?\$\$|\$.*?\$", " ", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"\\\[.*?\\\]|\\\(.*?\\\)", " ", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"\\begin\s*\{[^{}]*\}|\\end\s*\{[^{}]*\}", " ", cleaned)
    cleaned = re.sub(r"\\[A-Za-z@]+\*?(?:\s*\[[^\]]*\])*", " ", cleaned)
    cleaned = cleaned.translate(str.maketrans({"{": " ", "}": " ", "~": " ", "&": " "}))
    tokens = re.findall(
        r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*|[\u3400-\u4dbf\u4e00-\u9fff]",
        cleaned,
    )
    return len(tokens)


def clean_title(title: str) -> str:
    title = re.sub(r"\\[A-Za-z@]+\*?", " ", title)
    title = re.sub(r"[{}~]", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def normalize_identifier(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", clean_title(value).lower()).strip()


SECTION_RE = re.compile(
    r"\\section\*?\s*(?:\[[^\]]*\]\s*)?\{([^{}]*)\}", re.DOTALL
)
SUBSECTION_RE = re.compile(
    r"\\subsection\*?\s*(?:\[[^\]]*\]\s*)?\{([^{}]*)\}", re.DOTALL
)
LABEL_RE = re.compile(r"\\label\s*\{([^{}]+)\}")
CITE_RE = re.compile(r"\\cite\w*\*?(?:\s*\[[^\]]*\])*\s*\{([^{}]+)\}")


def extract_sections(text: str) -> list[dict[str, Any]]:
    matches = list(SECTION_RE.finditer(text))
    occurrences: Counter[str] = Counter()
    sections: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        title = clean_title(match.group(1))
        normalized = normalize_identifier(title)
        occurrences[normalized] += 1
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.start() : end]
        sections.append(
            {
                "id": f"{normalized}#{occurrences[normalized]}",
                "title": title,
                "normalized_title": normalized,
                "raw_source_words": raw_source_words(body),
                "normalized_words": normalized_words(body),
                "labels": sorted(set(LABEL_RE.findall(body))),
            }
        )
    return sections


def extract_citations(text: str) -> list[str]:
    citations: set[str] = set()
    for group in CITE_RE.findall(text):
        citations.update(item.strip() for item in group.split(",") if item.strip())
    return sorted(citations)


def count_environments(text: str, names: tuple[str, ...]) -> int:
    choices = "|".join(re.escape(name) for name in names)
    return len(re.findall(rf"\\begin\s*\{{(?:{choices})\*?\}}", text))


def structure_metrics(text: str) -> dict[str, Any]:
    return {
        "sections": len(SECTION_RE.findall(text)),
        "subsections": len(SUBSECTION_RE.findall(text)),
        "equations": count_environments(
            text, ("equation", "align", "alignat", "gather", "multline", "displaymath")
        )
        + len(re.findall(r"\\\[", text)),
        "propositions_theorems": count_environments(
            text, ("proposition", "theorem", "lemma", "corollary")
        ),
        "tables": count_environments(text, ("table", "longtable")),
        "figures": count_environments(text, ("figure",)),
        "labels": sorted(set(LABEL_RE.findall(text))),
        "citations": extract_citations(text),
    }


def manuscript_metrics(text: str) -> dict[str, Any]:
    metrics = {
        "raw_source_words": raw_source_words(text),
        "normalized_words": normalized_words(text),
        "structure": structure_metrics(text),
        "section_metrics": extract_sections(text),
    }
    return metrics


def load_contract(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise MetricUnavailable(f"cannot read artifact contract: {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise MetricUnavailable("artifact contract must be a JSON object")
    nested = payload.get("artifact_contract", payload)
    if not isinstance(nested, dict):
        raise MetricUnavailable("artifact_contract must be a JSON object")
    return nested


def number(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def range_pair(value: Any) -> tuple[float, float] | None:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        return None
    lower, upper = number(value[0]), number(value[1])
    if lower is None or upper is None or lower > upper:
        return None
    return lower, upper


def approval_scopes(contract: dict[str, Any]) -> set[str]:
    record = contract.get("approval_record", {})
    if not isinstance(record, dict) or not record.get("approved_by"):
        return set()
    scope = record.get("approved_scope", [])
    if isinstance(scope, str):
        scope = [scope]
    if not isinstance(scope, list):
        return set()
    return {str(item).strip().lower() for item in scope if str(item).strip()}


def compression_approved(contract: dict[str, Any], scopes: set[str]) -> bool:
    value = contract.get("user_approved_compression", False)
    if isinstance(value, bool) and value:
        return True
    if isinstance(value, dict) and value.get("approved"):
        return True
    return bool({"all", "compression", "main_text_reduction"} & scopes)


def scope_allows(scopes: set[str], action: str, value: str) -> bool:
    normalized = normalize_identifier(value)
    candidates = {
        "all",
        action.lower(),
        f"{action.lower()}:{value.lower()}",
        f"{action.lower()}:{normalized}",
    }
    return bool(candidates & scopes)


def allowed_move_set(contract: dict[str, Any]) -> set[str]:
    value = contract.get("allowed_appendix_moves", [])
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return set()
    allowed: set[str] = set()
    for item in value:
        if isinstance(item, dict):
            raw = item.get("id") or item.get("value") or item.get("section") or item.get("label")
        else:
            raw = item
        if raw is not None:
            allowed.add(str(raw))
            allowed.add(normalize_identifier(str(raw)))
    return allowed


def selected_word_metric(contract: dict[str, Any], cli_value: str | None) -> str:
    if cli_value:
        return cli_value
    measurement = contract.get("measurement_contract", {})
    if isinstance(measurement, dict):
        method = measurement.get("source_word_method")
        if method in {"raw_source_words", "normalized_words"}:
            return str(method)
    return "normalized_words"


def reduction_pct(baseline: float, candidate: float) -> float | None:
    if baseline <= 0:
        return None
    return (baseline - candidate) / baseline


def structural_delta(baseline: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    delta: dict[str, Any] = {}
    for key in ("sections", "subsections", "equations", "propositions_theorems", "tables", "figures"):
        delta[key] = candidate[key] - baseline[key]
    baseline_labels, candidate_labels = set(baseline["labels"]), set(candidate["labels"])
    baseline_cites, candidate_cites = set(baseline["citations"]), set(candidate["citations"])
    delta["labels_removed"] = sorted(baseline_labels - candidate_labels)
    delta["labels_added"] = sorted(candidate_labels - baseline_labels)
    delta["citations_removed"] = sorted(baseline_cites - candidate_cites)
    delta["citations_added"] = sorted(candidate_cites - baseline_cites)
    return delta


def main_label_to_section(sections: list[dict[str, Any]]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for section in sections:
        for label in section["labels"]:
            mapping[label] = section["normalized_title"]
    return mapping


def check_must_remain(
    contract: dict[str, Any], candidate_sections: list[dict[str, Any]], candidate_labels: set[str]
) -> list[str]:
    requirements = contract.get("must_remain_main", [])
    if isinstance(requirements, (str, dict)):
        requirements = [requirements]
    if not isinstance(requirements, list):
        return ["must_remain_main has an invalid type"]
    section_names = {section["normalized_title"] for section in candidate_sections}
    missing: list[str] = []
    for requirement in requirements:
        if isinstance(requirement, dict):
            kind = str(requirement.get("type", "")).lower()
            value = str(requirement.get("value") or requirement.get("id") or "").strip()
        else:
            kind, value = "either", str(requirement).strip()
        if not value:
            continue
        present = False
        if kind in {"label", "either"} and value in candidate_labels:
            present = True
        if kind in {"section", "title", "either"} and normalize_identifier(value) in section_names:
            present = True
        if not present:
            missing.append(value)
    return missing


def audit(args: argparse.Namespace) -> dict[str, Any]:
    baseline_path = Path(args.baseline).expanduser().resolve()
    candidate_path = Path(args.candidate).expanduser().resolve()
    contract_path = Path(args.contract).expanduser().resolve() if args.contract else None
    contract = load_contract(contract_path)

    if args.project_root:
        project_root = Path(args.project_root).expanduser().resolve()
    else:
        project_root = Path(
            os.path.commonpath([str(baseline_path.parent), str(candidate_path.parent)])
        ).resolve()
    if not project_root.is_dir():
        raise MetricUnavailable(f"project root is not a directory: {project_root}")

    baseline_text, baseline_sources = expand_tex(baseline_path, project_root)
    candidate_text, candidate_sources = expand_tex(candidate_path, project_root)
    baseline_main, baseline_appendix = split_appendix(
        baseline_text, args.appendix_marker, "baseline"
    )
    candidate_main, candidate_appendix = split_appendix(
        candidate_text, args.appendix_marker, "candidate"
    )

    baseline_metrics = manuscript_metrics(baseline_main)
    candidate_metrics = manuscript_metrics(candidate_main)
    baseline_appendix_metrics = manuscript_metrics(baseline_appendix)
    candidate_appendix_metrics = manuscript_metrics(candidate_appendix)
    metric_name = selected_word_metric(contract, args.word_metric)
    baseline_words = float(baseline_metrics[metric_name])
    candidate_words = float(candidate_metrics[metric_name])
    word_reduction = reduction_pct(baseline_words, candidate_words)
    if word_reduction is None:
        raise MetricUnavailable(f"baseline {metric_name} must be greater than zero")

    baseline_pages = number(args.baseline_main_pdf_pages)
    candidate_pages = number(args.candidate_main_pdf_pages)
    page_reduction = None
    if baseline_pages is not None and candidate_pages is not None:
        page_reduction = reduction_pct(baseline_pages, candidate_pages)

    baseline_sections = baseline_metrics["section_metrics"]
    candidate_sections = candidate_metrics["section_metrics"]
    candidate_appendix_sections = candidate_appendix_metrics["section_metrics"]
    baseline_counts = Counter(section["normalized_title"] for section in baseline_sections)
    candidate_counts = Counter(section["normalized_title"] for section in candidate_sections)
    appendix_counts = Counter(
        section["normalized_title"] for section in candidate_appendix_sections
    )
    baseline_titles = {
        section["normalized_title"]: section["title"] for section in baseline_sections
    }
    missing_sections: list[dict[str, Any]] = []
    for normalized, count in baseline_counts.items():
        missing_count = max(0, count - candidate_counts[normalized])
        moved_count = min(missing_count, appendix_counts[normalized])
        for index in range(missing_count):
            missing_sections.append(
                {
                    "title": baseline_titles[normalized],
                    "normalized_title": normalized,
                    "disposition": "moved_appendix" if index < moved_count else "missing",
                }
            )

    baseline_main_labels = set(baseline_metrics["structure"]["labels"])
    candidate_main_labels = set(candidate_metrics["structure"]["labels"])
    candidate_appendix_labels = set(candidate_appendix_metrics["structure"]["labels"])
    labels_moved_to_appendix = sorted(
        (baseline_main_labels - candidate_main_labels) & candidate_appendix_labels
    )
    label_source_sections = main_label_to_section(baseline_sections)

    allowed_moves = allowed_move_set(contract)
    scopes = approval_scopes(contract)
    failures: list[str] = []
    approval_triggers: list[str] = []
    warnings: list[str] = []

    for section in missing_sections:
        title = section["title"]
        normalized = section["normalized_title"]
        if section["disposition"] == "moved_appendix":
            authorized = (
                title in allowed_moves
                or normalized in allowed_moves
                or scope_allows(scopes, "move_appendix", title)
            )
            if not authorized:
                failures.append(f"unapproved whole-section appendix move: {title}")
        elif not scope_allows(scopes, "delete", title):
            failures.append(f"unapproved whole-section disappearance: {title}")

    for label in labels_moved_to_appendix:
        source_section = label_source_sections.get(label, "")
        authorized = (
            label in allowed_moves
            or source_section in allowed_moves
            or scope_allows(scopes, "move_appendix", label)
        )
        if not authorized:
            failures.append(f"unapproved label moved to appendix: {label}")

    missing_required = check_must_remain(contract, candidate_sections, candidate_main_labels)
    for item in missing_required:
        failures.append(f"must_remain_main missing: {item}")

    floor_value = contract.get("hard_main_text_floor", {})
    if isinstance(floor_value, (int, float)) and not isinstance(floor_value, bool):
        floor_words = float(floor_value)
        floor_pages = None
    elif isinstance(floor_value, dict):
        floor_words = number(floor_value.get("source_words"))
        floor_pages = number(floor_value.get("pdf_pages"))
    else:
        floor_words = floor_pages = None
    if args.min_main_source_words is not None:
        floor_words = float(args.min_main_source_words)
    if args.min_main_pdf_pages is not None:
        floor_pages = float(args.min_main_pdf_pages)

    if floor_words is not None and candidate_words < floor_words:
        failures.append(
            f"candidate {metric_name} {candidate_words:.0f} is below hard floor {floor_words:.0f}"
        )
    if floor_pages is not None:
        if candidate_pages is None:
            raise MetricUnavailable(
                "a main-text PDF page floor is set but --candidate-main-pdf-pages is unavailable"
            )
        if candidate_pages < floor_pages:
            failures.append(
                f"candidate main PDF pages {candidate_pages:.0f} are below hard floor {floor_pages:.0f}"
            )

    target_words = range_pair(contract.get("target_main_source_word_range"))
    if target_words and not (target_words[0] <= candidate_words <= target_words[1]):
        failures.append(
            f"candidate {metric_name} {candidate_words:.0f} is outside target range "
            f"[{target_words[0]:.0f}, {target_words[1]:.0f}]"
        )
    target_pages = range_pair(contract.get("target_main_pdf_page_range"))
    if target_pages:
        if candidate_pages is None:
            raise MetricUnavailable(
                "a main-text PDF page target is set but --candidate-main-pdf-pages is unavailable"
            )
        if not (target_pages[0] <= candidate_pages <= target_pages[1]):
            failures.append(
                f"candidate main PDF pages {candidate_pages:.0f} are outside target range "
                f"[{target_pages[0]:.0f}, {target_pages[1]:.0f}]"
            )

    task_mode = str(contract.get("task_mode", "")).lower()
    mature = contract.get("mature_baseline") is True or task_mode in {
        "major_revision",
        "restructure",
    }
    shortening_requested = task_mode in {"shorten", "short_form"}
    explicit_shorter = shortening_requested and bool(
        target_words or target_pages or compression_approved(contract, scopes)
    )
    if shortening_requested and not explicit_shorter:
        failures.append(
            "shorten mode requires a recorded target range or explicit compression approval"
        )
    maximum = number(args.max_main_reduction)
    if maximum is None:
        maximum = number(contract.get("max_unapproved_main_reduction_pct"))
    if maximum is None and mature and not explicit_shorter:
        maximum = 0.15
    reductions = [word_reduction]
    if page_reduction is not None:
        reductions.append(page_reduction)
    cumulative_reduction = max(reductions)
    if (
        maximum is not None
        and cumulative_reduction > maximum
        and not explicit_shorter
        and not compression_approved(contract, scopes)
    ):
        approval_triggers.append(
            f"cumulative main-text reduction {cumulative_reduction:.1%} exceeds "
            f"unapproved limit {maximum:.1%}"
        )

    if candidate_metrics["structure"]["sections"] == 0:
        warnings.append("candidate main text contains no detected section commands")

    if failures:
        status = "fail"
    elif approval_triggers:
        status = "approval_required"
    else:
        status = "pass"

    baseline_by_id = {item["id"]: item for item in baseline_sections}
    candidate_by_id = {item["id"]: item for item in candidate_sections}
    section_changes: list[dict[str, Any]] = []
    for section_id in sorted(set(baseline_by_id) | set(candidate_by_id)):
        before = baseline_by_id.get(section_id)
        after = candidate_by_id.get(section_id)
        section_changes.append(
            {
                "section_id": section_id,
                "title": (after or before or {}).get("title"),
                "baseline_raw_source_words": before and before["raw_source_words"],
                "candidate_raw_source_words": after and after["raw_source_words"],
                "baseline_normalized_words": before and before["normalized_words"],
                "candidate_normalized_words": after and after["normalized_words"],
            }
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "exit_code": EXIT_CODES[status],
        "inputs": {
            "baseline": str(baseline_path),
            "baseline_sha256": sha256_file(baseline_path),
            "candidate": str(candidate_path),
            "candidate_sha256": sha256_file(candidate_path),
            "project_root": str(project_root),
            "contract": str(contract_path) if contract_path else None,
            "appendix_marker": args.appendix_marker,
            "baseline_sources": sorted(set(baseline_sources)),
            "candidate_sources": sorted(set(candidate_sources)),
        },
        "measurement": {
            "word_metric_for_contract": metric_name,
            "baseline_main_pdf_pages": baseline_pages,
            "candidate_main_pdf_pages": candidate_pages,
            "page_metric_note": "main-text page counts must use an explicit appendix boundary; total PDF pages are not accepted",
        },
        "metrics": {
            "baseline_main": baseline_metrics,
            "candidate_main": candidate_metrics,
            "baseline_appendix": baseline_appendix_metrics,
            "candidate_appendix": candidate_appendix_metrics,
            "word_reduction_pct": word_reduction,
            "page_reduction_pct": page_reduction,
            "cumulative_reduction_pct": cumulative_reduction,
            "max_unapproved_main_reduction_pct": maximum,
            "structural_delta": structural_delta(
                baseline_metrics["structure"], candidate_metrics["structure"]
            ),
            "section_changes": section_changes,
        },
        "conservation": {
            "whole_sections_missing_or_moved": missing_sections,
            "labels_moved_to_appendix": labels_moved_to_appendix,
            "must_remain_main_missing": missing_required,
        },
        "findings": {
            "failures": sorted(set(failures)),
            "approval_triggers": sorted(set(approval_triggers)),
            "warnings": sorted(set(warnings)),
        },
    }


def unavailable_report(args: argparse.Namespace, error: Exception) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "metric_unavailable",
        "exit_code": EXIT_CODES["metric_unavailable"],
        "inputs": {
            "baseline": str(Path(args.baseline).expanduser()),
            "candidate": str(Path(args.candidate).expanduser()),
            "project_root": args.project_root,
            "contract": args.contract,
            "appendix_marker": args.appendix_marker,
        },
        "findings": {
            "failures": [],
            "approval_triggers": [],
            "warnings": [str(error)],
        },
    }


def parser() -> argparse.ArgumentParser:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--baseline", required=True, help="Accepted baseline .tex entry point")
    cli.add_argument("--candidate", required=True, help="Candidate .tex entry point")
    cli.add_argument("--project-root", help="Root that bounds recursive input/include resolution")
    cli.add_argument("--contract", help="JSON artifact contract or object containing artifact_contract")
    cli.add_argument("--appendix-marker", default=r"\appendix")
    cli.add_argument(
        "--word-metric", choices=("raw_source_words", "normalized_words")
    )
    cli.add_argument("--max-main-reduction", type=float)
    cli.add_argument("--min-main-source-words", type=int)
    cli.add_argument("--baseline-main-pdf-pages", type=float)
    cli.add_argument("--candidate-main-pdf-pages", type=float)
    cli.add_argument("--min-main-pdf-pages", type=float)
    cli.add_argument("--report", required=True, help="Machine-readable JSON output")
    return cli


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        report = audit(args)
    except MetricUnavailable as exc:
        report = unavailable_report(args, exc)
    report_path = Path(args.report).expanduser()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    status = report["status"]
    metrics = report.get("metrics", {})
    reduction = metrics.get("cumulative_reduction_pct")
    reduction_text = f"; cumulative reduction={reduction:.1%}" if reduction is not None else ""
    print(f"conservation audit: {status}{reduction_text}; report={report_path}")
    for item in report.get("findings", {}).get("failures", []):
        print(f"FAIL: {item}")
    for item in report.get("findings", {}).get("approval_triggers", []):
        print(f"APPROVAL: {item}")
    for item in report.get("findings", {}).get("warnings", []):
        print(f"WARNING: {item}")
    return EXIT_CODES[status]


if __name__ == "__main__":
    sys.exit(main())
