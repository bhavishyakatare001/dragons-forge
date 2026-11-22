# CPU Agent Research Pipeline

A four-stage pipeline, written in plain Python, that searches for academic papers on CPU scheduling algorithms, filters out irrelevant ones, stores extracted data in a local SQLite database and writes a markdown report.

## How it works

```
Search  ->  Validator  ->  Auditor  ->  Synthesis
```

| Stage | File | What it does |
|---|---|---|
| Search ("The Hunter") | `search.py` | Queries the ArXiv API, or scans a local folder of `.txt` files (`api`, `local` or `hybrid` mode). Removes duplicate titles. |
| Validator ("The Gatekeeper") | `validator.py` | Keeps only papers whose title or abstract mention terms such as *time quantum*, *waiting time* or *burst time*. |
| Auditor ("The Analyst") | `auditor.py` | Writes a markdown file per paper to `refined_papers/` and stores metrics in `synthesiser.db`. |
| Synthesis ("The Writer") | `synthesis.py` | Reads the database and writes `FINAL_RESEARCH_REPORT.md` with a citation for each point. |

`main.py` clears old output and runs all four stages.

## Run it

Python 3 and the standard library only, no installs. The search stage needs an internet connection for ArXiv.

```bash
cd cpu-agent-research
python main.py
```

Change the search topic by editing `research_query` in `main.py`.

## Current limitations

- **The Auditor's metric extraction is a placeholder.** `extract_metrics_mock()` does not read values from the paper. It returns fixed text when keywords such as "quantum" appear in the abstract. The generated report shows the pipeline working end to end, but its metric lines are **not real findings from the cited papers**.
- The Validator uses keyword matching, so it can miss relevant papers and pass loosely related ones.
- Only the first 3 ArXiv results are fetched by default.

## Next steps

- Replace `extract_metrics_mock()` with real extraction, for example a local model through Ollama that reads each abstract
- Add tests for the Validator and a way to evaluate its accuracy
