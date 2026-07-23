"""
HARVARD CS50 PYTHON - Week 6: File I/O (CSV Handling)
=======================================================
Concepts: CSV files, csv.reader(), csv.DictReader(), csv.DictWriter(), sorting

Author: David J. Malan (CS50)
Learning Level: Intermediate → Advanced | Best Practice: ✅
"""

import csv

# =============================================================================
# V1: Manual CSV Parsing — Splitting by comma (brittle!)
# =============================================================================
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
# 💡 WARNING: This breaks if a value contains a comma!
# 💡 split(",") is NOT a robust CSV parser

# =============================================================================
# V2: DICT READ — Read CSV with headers into dictionaries
# =============================================================================
# students = []
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
# 💡 lambda student: student["name"] = anonymous function that gets sort key
# 💡 csv.DictReader uses FIRST ROW as column headers automatically

# =============================================================================
# BEST PRACTICE: WRITE CSV — Using DictWriter
# =============================================================================

def add_student() -> None:
    """Add a new student to the CSV file."""
    name = input("What's your name? ").strip().title()
    home = input("What's your home? ").strip().title()

    with open("students.csv", "a", newline="") as file:    # 💡 newline="" prevents blank rows
        writer = csv.DictWriter(file, fieldnames=["name", "home"])

        # 💡 Check if file is empty to write header
        import os
        if os.stat("students.csv").st_size == 0:
            writer.writeheader()  # Writes "name,home" header row

        # 💡 Order of dict keys doesn't matter! fieldnames controls column order
        writer.writerow({"home": home, "name": name})

    print(f"✅ Added {name} from {home} to students.csv")


# =============================================================================
# BEST PRACTICE: READ CSV — Using DictReader with sorting
# =============================================================================

def list_students() -> None:
    """Read and display all students sorted by name."""
    students = []

    try:
        with open("students.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)  # row is already a dict!

        if not students:
            print("📭 No students found.")
            return

        print("\n📋 Student List:")
        for student in sorted(students, key=lambda s: s["name"]):
            print(f"  • {student['name']} — from {student['home']}")

    except FileNotFoundError:
        print("📭 No students.csv file found. Add students first!")


def main() -> None:
    """Demonstrate CSV read and write operations."""
    print("=== CSV File I/O Demo ===")

    # Uncomment to add a student:
    # add_student()

    # Display existing students
    list_students()


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ ALWAYS use csv module for CSV files — NOT manual split(",")
#   ✅ csv.DictReader = first row becomes headers, rest become dicts
#   ✅ csv.DictWriter with fieldnames controls column ORDER
#   ✅ sorted(list, key=function) = sort by custom key
#   ✅ lambda s: s["name"] = anonymous function that returns the sort value
#   ✅ newline="" prevents extra blank rows in CSV output

