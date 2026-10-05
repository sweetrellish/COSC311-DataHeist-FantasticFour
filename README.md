# SU - COSC311 Project - Data Heist: Fantastic Four

Shared workspace for COSC 311 Project 1, **Data Heist at StreamBeats**. The team is recovering a damaged listening-history log, analyzing the recovered events, and reporting useful findings to StreamBeats. See [Project1-DataHeist.pdf](Project1-DataHeist.pdf) for the complete assignment and grading requirements.

## Project Folders

Each part has a folder for its lead to develop and document that work. Coordinate shared code and results with the rest of the team so the final notebook runs from beginning to end.

| Folder | What belongs here |
| --- | --- |
| `Part1-DataModel/` | `Song`, `Listener`, and `ListeningEvent` classes, plus a brief explanation of the design. |
| `Part2-CorruptedArchive/` | Log generation and recovery: `dataGeneration.py`, the team-specific `streambeats_log.txt`, `parse_line()`, recovered events, and `recovery_report.txt`. **Current lead: you (Part 2).** |
| `Part3-Investigation/` | NumPy and pandas analysis: genre listening time, artist and song findings, popularity scores, charts, and the day-by-genre pivot. |
| `Part4-CaseFile/` | The plain-language leadership report: three evidence-backed findings, recovery rate and corruption summary, and one recommendation. |

| Part | Lead |
| --- | --- |
| Part 1: Data Model | Tanner |
| Part 2: Corrupted Archive | Ryan |
| Part 3: Investigation | Dylan |
| Part 4: Case File | Everyone contributes; Shelby compiles report. |

The assignment describes three rotating technical roles: Data Architect (Part 1), Recovery Engineer (Part 2), and Insights Analyst (Part 3). Part 4 uses the team's analysis to write the leadership report, so coordinate its findings with the Part 3 lead. Include a contribution log in the notebook.

## Final Deliverables

Combine the work into one team notebook named `teamname_project1.ipynb` (lowercase team name, no spaces). Keep the finished notebook and its exported `teamname_project1.pdf` at the repository root, unless the team agrees on another shared location. Include the generated `streambeats_log.txt` and `recovery_report.txt` with the submission.

Before submitting, restart the notebook kernel and run all cells in order. Check that the recovery report gives the total log lines, recovered events, and skipped lines; the notebook includes all required analysis, charts, the Insights Report, and the contribution log. Submit the notebook, PDF, log, and recovery report to MyClass/project1. One team member submits on behalf of the group.
