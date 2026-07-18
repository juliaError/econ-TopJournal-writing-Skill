#!/usr/bin/env python3
"""Synthetic regression tests for audit_manuscript_conservation.py."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("audit_manuscript_conservation.py")


class ConservationAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def contract(self, payload: dict) -> Path:
        return self.write(
            "contract.json",
            json.dumps({"artifact_contract": payload}, ensure_ascii=False),
        )

    def run_audit(
        self,
        baseline: Path,
        candidate: Path,
        contract: Path | None = None,
        *extra: str,
    ) -> tuple[subprocess.CompletedProcess[str], dict]:
        report = self.root / "report.json"
        command = [
            sys.executable,
            str(SCRIPT),
            "--baseline",
            str(baseline),
            "--candidate",
            str(candidate),
            "--project-root",
            str(self.root),
            "--report",
            str(report),
        ]
        if contract:
            command.extend(["--contract", str(contract)])
        command.extend(extra)
        completed = subprocess.run(command, text=True, capture_output=True, check=False)
        return completed, json.loads(report.read_text(encoding="utf-8"))

    def test_reorder_only_passes(self) -> None:
        baseline = self.write(
            "baseline.tex",
            r"""
\section{Data}\label{sec:data}
We describe the sample, variables, period, and measurement in full.
\section{Results}\label{sec:results}
The benchmark estimate, magnitude, and interpretation answer the question.
\appendix
\section{Supplement}
Additional detail.
""",
        )
        candidate = self.write(
            "candidate.tex",
            r"""
\section{Results}\label{sec:results}
The benchmark estimate, magnitude, and interpretation answer the question.
\section{Data}\label{sec:data}
We describe the sample, variables, period, and measurement in full.
\appendix
\section{Supplement}
Additional detail.
""",
        )
        contract = self.contract(
            {"task_mode": "restructure", "mature_baseline": True}
        )
        completed, report = self.run_audit(baseline, candidate, contract)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(report["status"], "pass")

    def test_unapproved_appendix_migration_fails(self) -> None:
        baseline = self.write(
            "baseline.tex",
            r"""
\section{Data and Sample}\label{sec:data}
The main text defines the sample, construction, exclusions, and audit.
\section{Results}\label{sec:results}
The main estimate is economically large and precisely benchmarked.
\appendix
\section{Extra checks}
Details.
""",
        )
        candidate = self.write(
            "candidate.tex",
            r"""
\section{Results}\label{sec:results}
The main estimate is economically large and precisely benchmarked.
\appendix
\section{Data and Sample}\label{sec:data}
The appendix defines the sample, construction, exclusions, and audit.
""",
        )
        contract = self.contract(
            {
                "task_mode": "restructure",
                "mature_baseline": True,
                "must_remain_main": [{"type": "label", "value": "sec:data"}],
            }
        )
        completed, report = self.run_audit(baseline, candidate, contract)
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(report["status"], "fail")
        findings = " ".join(report["findings"]["failures"])
        self.assertIn("appendix move", findings)
        self.assertIn("must_remain_main", findings)

    def test_authorized_proof_only_migration_passes(self) -> None:
        baseline = self.write(
            "baseline.tex",
            r"""
\section{Theory}\label{sec:theory}
Agents face a constraint, change behavior, and generate the stated proposition.
The main text explains assumptions, mechanism, interpretation, and prediction.
\section{Proofs}\label{sec:proofs}
The algebra establishes the proposition step by step.
\appendix
\section{Other material}
Details.
""",
        )
        candidate = self.write(
            "candidate.tex",
            r"""
\section{Theory}\label{sec:theory}
Agents face a constraint, change behavior, and generate the stated proposition.
The main text explains assumptions, mechanism, interpretation, and prediction.
The formal proof appears in the appendix while its economic content remains here.
\appendix
\section{Proofs}\label{sec:proofs}
The algebra establishes the proposition step by step.
""",
        )
        contract = self.contract(
            {
                "task_mode": "restructure",
                "mature_baseline": True,
                "max_unapproved_main_reduction_pct": 0.50,
                "allowed_appendix_moves": ["Proofs"],
                "must_remain_main": ["sec:theory"],
            }
        )
        completed, report = self.run_audit(baseline, candidate, contract)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(report["status"], "pass")

    def test_authorized_short_form_ignores_default_fifteen_percent_gate(self) -> None:
        long_text = " ".join(["baseline discussion"] * 120)
        short_text = " ".join(["concise evidence"] * 25)
        baseline = self.write(
            "baseline.tex",
            f"\\section{{Analysis}}\n{long_text}\n\\appendix\n\\section{{Notes}}\nExtra.",
        )
        candidate = self.write(
            "candidate.tex",
            f"\\section{{Analysis}}\n{short_text}\n\\appendix\n\\section{{Notes}}\nExtra.",
        )
        contract = self.contract(
            {
                "task_mode": "shorten",
                "mature_baseline": True,
                "target_main_source_word_range": [20, 80],
                "max_unapproved_main_reduction_pct": 0.15,
                "user_approved_compression": True,
                "target_basis": "user",
            }
        )
        completed, report = self.run_audit(baseline, candidate, contract)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(report["status"], "pass")
        self.assertGreater(report["metrics"]["cumulative_reduction_pct"], 0.15)

    def test_unapproved_reduction_returns_approval_required(self) -> None:
        baseline = self.write(
            "baseline.tex",
            "\\section{Analysis}\n" + "evidence mechanism " * 100 + "\n\\appendix\nExtra.",
        )
        candidate = self.write(
            "candidate.tex",
            "\\section{Analysis}\n" + "evidence mechanism " * 60 + "\n\\appendix\nExtra.",
        )
        contract = self.contract(
            {"task_mode": "major_revision", "mature_baseline": True}
        )
        completed, report = self.run_audit(baseline, candidate, contract)
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(report["status"], "approval_required")

    def test_shorten_mode_without_target_or_approval_fails(self) -> None:
        baseline = self.write(
            "baseline.tex",
            "\\section{Analysis}\n" + "full evidence " * 40 + "\n\\appendix\nExtra.",
        )
        candidate = self.write(
            "candidate.tex",
            "\\section{Analysis}\n" + "full evidence " * 20 + "\n\\appendix\nExtra.",
        )
        contract = self.contract(
            {"task_mode": "shorten", "mature_baseline": True}
        )
        completed, report = self.run_audit(baseline, candidate, contract)
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(report["status"], "fail")
        self.assertIn("requires a recorded target", report["findings"]["failures"][0])

    def test_missing_appendix_marker_is_metric_unavailable(self) -> None:
        baseline = self.write("baseline.tex", r"\section{Analysis} Complete text.")
        candidate = self.write("candidate.tex", r"\section{Analysis} Complete text.")
        completed, report = self.run_audit(baseline, candidate)
        self.assertEqual(completed.returncode, 3)
        self.assertEqual(report["status"], "metric_unavailable")
        self.assertIn("found 0", report["findings"]["warnings"][0])

    def test_multiple_appendix_markers_are_metric_unavailable(self) -> None:
        baseline = self.write(
            "baseline.tex", r"\section{Analysis} Text.\appendix One.\appendix Two."
        )
        candidate = self.write(
            "candidate.tex", r"\section{Analysis} Text.\appendix One."
        )
        completed, report = self.run_audit(baseline, candidate)
        self.assertEqual(completed.returncode, 3)
        self.assertEqual(report["status"], "metric_unavailable")
        self.assertIn("found 2", report["findings"]["warnings"][0])

    def test_nested_inputs_and_commented_marker_pass(self) -> None:
        self.write(
            "parts/body.tex",
            r"""
\section{Data}\label{sec:data}
Sample and measurement details remain in the main text.
\input{nested/results}
""",
        )
        self.write(
            "parts/nested/results.tex",
            r"""
\section{Results}\label{sec:results}
Magnitude, benchmark, and interpretation remain in the main text.
""",
        )
        root_text = r"""
% \appendix is a comment and must not set the boundary
\input{parts/body}
\appendix
\section{Supplement}
Additional details.
"""
        baseline = self.write("baseline.tex", root_text)
        candidate = self.write("candidate.tex", root_text)
        contract = self.contract(
            {"task_mode": "restructure", "mature_baseline": True}
        )
        completed, report = self.run_audit(baseline, candidate, contract)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(report["status"], "pass")
        self.assertEqual(len(report["inputs"]["baseline_sources"]), 3)

    def test_pdf_floor_requires_main_page_metric(self) -> None:
        source = r"\section{Analysis} Complete text.\appendix Extra."
        baseline = self.write("baseline.tex", source)
        candidate = self.write("candidate.tex", source)
        contract = self.contract(
            {
                "task_mode": "restructure",
                "mature_baseline": True,
                "hard_main_text_floor": {"pdf_pages": 15},
            }
        )
        completed, report = self.run_audit(baseline, candidate, contract)
        self.assertEqual(completed.returncode, 3)
        self.assertEqual(report["status"], "metric_unavailable")
        self.assertIn("main-text PDF page floor", report["findings"]["warnings"][0])


if __name__ == "__main__":
    unittest.main()
