# Student Grade Analyzer — Day 6

A Python CLI application to manage and analyze student grades, built with OOP principles, file handling, and input validation.

---

## Features

- Add, view, update, and delete students
- Calculate individual averages and letter grades
- Find class topper and highest/lowest averages
- Calculate class average
- Search students by name
- Sort students alphabetically
- Save and load data as JSON
- Export and import data as CSV
- Generate timestamped performance reports
- Input validation with duplicate detection

---

## Project Structure

```
student-grade-analyzer-v6/
├── main.py          # Entry point — menu loop and routing
├── student.py       # Student class with average, grade, display logic
├── utils.py         # All menu-driven functions (add, delete, search, etc.)
├── file_handler.py  # JSON and CSV read/write operations
├── validator.py     # Input validation (name, marks, duplicates)
└── .gitignore       # Ignores __pycache__, reports, data files
```

---

## How to Run

```bash
python main.py
```

No external libraries required — uses Python standard library only (`json`, `csv`, `logging`, `pathlib`, `datetime`).

---

## Grade Scale

| Average | Grade |
|---------|-------|
| 90 – 100 | A+ |
| 80 – 89  | A  |
| 70 – 79  | B  |
| 60 – 69  | C  |
| 50 – 59  | D  |
| 40 – 49  | E  |
| Below 40 | F  |

---

## What I Learned — Day 6

- File handling with `json` and `csv` modules
- Using `csv.DictWriter` and `csv.DictReader` for structured data
- Consistent error handling with Python `logging` module
- Input validation and raising custom `ValueError` / `TypeError`
- Generating timestamped reports using `datetime` and `pathlib`
- Using `.gitignore` to keep repos clean

---

## Roadmap

- **Day 7** — Clean Architecture Refactor: split into `services/`, `storage/`, and `ui/` layers
