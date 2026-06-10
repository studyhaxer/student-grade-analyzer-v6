# Student Grade Analyzer V5

A command-line Python application to manage and analyze student grades. Built as part of a daily Python learning series.

## Features

- Add, view, update, and delete students
- Search students by name
- Calculate individual averages and letter grades
- Find class topper, highest and lowest averages
- Calculate class average
- Sort students by name
- Save and load students from a JSON file
- Input validation and error handling throughout

## Project Structure

```
student-grade-analyzer-v5/
├── main.py          # Entry point, menu loop
├── student.py       # Student class (average, grade, display)
├── utils.py         # All menu functions (add, view, search, etc.)
├── validator.py     # Input validation (name, marks, duplicates)
├── file_handler.py  # Save and load students to/from JSON
└── .gitignore
```

## Grading Scale

| Average | Grade |
|---------|-------|
| 90 – 100 | A+  |
| 80 – 89  | A   |
| 70 – 79  | B   |
| 60 – 69  | C   |
| 50 – 59  | D   |
| 40 – 49  | E   |
| Below 40 | F   |

## How to Run

```bash
python main.py
```

## Menu Options

```
1.  Add Students
2.  View Students
3.  Topper
4.  Save Students
5.  Load Students
6.  Search Students
7.  Total Students
8.  Class Average
9.  Delete Students
10. Update Students
11. Sort Students by Name
12. Highest and Lowest Averages
13. Save and Exit
```

## What's New in V5

- Split into multiple modules (previously single file)
- Centralized validation in `validator.py`
- Logging added across all modules
- Fixed menu input bug for non-integer input
- Edge case handled: empty marks list no longer crashes

## Requirements

- Python 3.x
- No external libraries required

## Learning Series

| Day | Version | Focus |
|-----|---------|-------|
| Day 1 | V1 | Basic add/view/grade logic |
| Day 2 | V2 | Loops, input validation |
| Day 3 | V3 | File handling (JSON) |
| Day 4 | V4 | Search, sort, update, delete |
| Day 5 | V5 | Modular structure, logging, validation module |
