# Lab 5 — Static Code Analysis (Online Examination System)

**Name:** Kashvi Madhu
**SRN:** PES1UG24CS221
**Assigned task:** `L5_34_online_exam`
**Original working repo:** https://github.com/ReachKashvi/L5_34_online_exam
(fork of `SETAPESU26/L5_34_online_exam` — copied here so Labs 5, 6 and 7 sit together)

## Files

| File | Description |
|------|-------------|
| `README_task.md` | The lab task README as given |
| `online_exam_ORIGINAL_backup.py` | The program before any fixes |
| `online_exam.py` | The program after fixing all static-analysis findings |
| `program_output_before.txt` | Program output before the fixes |
| `program_output_after.txt` | Program output after the fixes (behaviour unchanged) |
| `pylint_report.txt` / `pylint_report_after.txt` | Pylint, before and after |
| `flake8_report.txt` / `flake8_report_after.txt` | Flake8, before and after |
| `bandit_report.txt` / `bandit_report_after.txt` | Bandit, before and after |
| `issues.md` | Every finding, with cause and fix |
| `reflection.md` | Write-up / reflection |
| `demo/old_mod.py`, `demo/new_mod.py` | Before/after comparison copies used in the demo |

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | findings across style, naming and design | **10.00/10** |
| Flake8 | style violations reported | **0 findings** (empty report) |
| Bandit | MD5 hashing, mutable default, `os.system` command injection | **0 issues** (all severities) |

Program behaviour is unchanged by the fixes — compare `program_output_before.txt`
with `program_output_after.txt` (the bonus question is random, so only that first
line differs between runs).

## How to run

```bash
python -m pip install pylint bandit flake8

python online_exam.py

pylint online_exam.py
flake8 online_exam.py
bandit -r online_exam.py
```
