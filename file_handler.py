import logging
import json
import csv
from student import Student
def save_students(students, filename="students.json"):
    std_data = []
    for student in students:
        std_data.append(student.to_dict())
    try:
        with open(filename, 'w') as file:
            json.dump(std_data, file, indent=4)
        logging.info("Students saved successfully.")
    except Exception as e:
        logging.error(f"Error saving students: {e}")
def load_students(students, filename="students.json"):
    """Clears and repopulates the students list from a JSON file."""
    try:
        with open(filename, 'r') as file:
            std_data = json.load(file)
            students.clear()
            for std in std_data:
                student = Student(std["name"], std["marks"])
                students.append(student)
        logging.info("Students loaded successfully.")
    except FileNotFoundError:
        logging.error("Students file not found.")
    except json.JSONDecodeError:
        logging.error("File is corrupted or not valid JSON.")
    except KeyError as e:
        logging.error(f"Error: Missing expected field {e} in file. Students not loaded.")

def csv_write_dict(students, filename="students.csv"):
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = ["name", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                marks_str = ",".join(str(mark) for mark in student.marks)
                writer.writerow({"name": student.name, "marks": marks_str})
            logging.info("Data exported successfully.")
    except Exception as e:
        logging.error(f"Error writing CSV: {e}")
def csv_reader_dict(students, filename="students.csv"):
    try:
        students.clear()
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                marks_str = row["marks"].split(",")
                marks = [float(mark) for mark in marks_str]
                student = Student(name, marks)
                students.append(student)
            logging.info("Data imported successfully.")
    except Exception as e:
        logging.error(f"Error Reading CSV: {e}")
