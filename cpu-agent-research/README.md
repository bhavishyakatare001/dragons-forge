# CPU Agent Research Pipeline

An autonomous, multi-agent AI pipeline built entirely in Python. It is designed to fetch, filter, extract, and synthesize academic research papers (specifically focused on CPU scheduling algorithms) directly from the terminal.

### Architecture
* **The Hunter:** Interfaces with the ArXiv API to gather raw academic metadata.
* **The Gatekeeper:** Filters out irrelevant papers by ensuring strict adherence to targeted scheduling metrics.
* **The Analyst:** Extracts data into a local SQLite database (`synthesiser.db`) and generates clean `.md` files.
* **The Writer:** Synthesizes the database rows into a final, automatically cited research report.

### Usage
Run the master switchboard to execute the entire pipeline:
python main.py
