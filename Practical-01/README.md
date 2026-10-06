# Practical 01 - Parsing, Anomaly Checks, Binary/Pickle, Regex, SQLite CRUD

## Objective
Practice multi-format parsing (TXT, CSV, HTML, XML, JSON), basic data-quality
checks, binary and pickle file handling, regex operations, and a relational
SQLite database with CRUD.

## Contents
- `setup_data.py`
- `ex1_parsing_and_anomalies.py`
- `ex2_binary_files.py`
- `ex3_regex_operations.py`
- `ex4_database_crud.py`
- Sample files: `sample.txt`, `sample.csv`, `sample.html`, `sample.xml`, `sample.json`
- Artifacts (generated at runtime): `records.bin`, `app.pkl`, `app.db`

## Prerequisites
- Python 3.10+
- `beautifulsoup4` (for HTML parsing in `ex1_parsing_and_anomalies.py`)

## Dependency install
```bash
pip install beautifulsoup4