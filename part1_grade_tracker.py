# ============================================================
# Part 1: Student Grade Tracker
# ============================================================

# ============================================================
# Task 1 — Data Parsing & Profile Cleaning (5 marks)
# ============================================================

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []  # will store all cleaned student dicts

for student in raw_students:
    # Clean name: strip whitespace, convert to Title Case
    clean_name  = student["name"].strip().title()
    # Convert roll from string to integer
    clean_roll  = int(student["roll"])
    # Split marks string on ", " and convert each to int
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]

    # Validate name: every word must be alphabetic only
    words    = clean_name.split()
    is_valid = all(word.isalpha() for word in words)
    validity = "✓ Valid name" if is_valid else "✗ Invalid name"

    # Store cleaned student
    cleaned_students.append({
        "name":  clean_name,
        "roll":  clean_roll,
        "marks": clean_marks
    })

    # Print profile card
    print("================================")
    print(f"Student : {clean_name}  {validity}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("================================")

# Find student with roll number 103 and print ALL CAPS and lowercase
for student in cleaned_students:
    if student["roll"] == 103:
        print(f"\nRoll 103 Name in ALL CAPS : {student['name'].upper()}")
        print(f"Roll 103 Name in lowercase: {student['name'].lower()}")


# ============================================================
# Task 2 — Marks Analysis Using Loops & Conditionals (8 marks)
# ============================================================

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# Grade helper function
def get_grade(m):
    if m >= 90:   return "A+"
    elif m >= 80: return "A"
    elif m >= 70: return "B"
    elif m >= 60: return "C"
    else:         return "F"

print(f"\nMarks Report for: {student_name}")
print("-" * 35)

# For loop: print each subject, marks, and grade
for subject, mark in zip(subjects, marks):
    grade = get_grade(mark)
    print(f"{subject:<12}: {mark}  [{grade}]")

# Summary stats
total   = sum(marks)
average = round(total / len(marks), 2)

# Highest and lowest using manual loop (avoids built-in max/min)
highest_mark = marks[0]
lowest_mark  = marks[0]
highest_sub  = subjects[0]
lowest_sub   = subjects[0]

for i in range(1, len(marks)):
    if marks[i] > highest_mark:
        highest_mark = marks[i]
        highest_sub  = subjects[i]
    if marks[i] < lowest_mark:
        lowest_mark = marks[i]
        lowest_sub  = subjects[i]

print("-" * 35)
print(f"Total Marks    : {total}")
print(f"Average Marks  : {average}")
print(f"Highest Subject: {highest_sub} ({highest_mark})")
print(f"Lowest Subject : {lowest_sub} ({lowest_mark})")

# While loop: simulate marks-entry system
print("\n--- Add New Subjects (type 'done' to stop) ---")

new_count = 0  # tracks valid subjects added

while True:
    subject_input = input("Enter subject name (or 'done' to stop): ").strip()

    if subject_input.lower() == "done":
        break  # exit when user types done

    marks_input = input(f"Enter marks for {subject_input} (0-100): ").strip()

    # Validate: must be numeric
    if not marks_input.isnumeric():
        print("⚠️  Warning: Invalid input — marks must be a number. Skipping.")
        continue

    marks_val = int(marks_input)

    # Validate: must be within 0–100
    if marks_val < 0 or marks_val > 100:
        print("⚠️  Warning: Marks must be between 0 and 100. Skipping.")
        continue

    # Valid — add to lists
    subjects.append(subject_input)
    marks.append(marks_val)
    new_count += 1
    print(f"✓ Added: {subject_input} — {marks_val}")

updated_average = round(sum(marks) / len(marks), 2)
print(f"\nNew subjects added : {new_count}")
print(f"Updated Average    : {updated_average}")


# ============================================================
# Task 3 — Class Performance Summary (7 marks)
# ============================================================

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print(f"\n{'Name':<18}| {'Average':<8}| Status")
print("-" * 40)

all_averages   = []  # store each student's average for class average
passed         = 0
failed         = 0
topper_name    = ""
topper_avg     = 0

for name, marks_list in class_data:
    avg    = round(sum(marks_list) / len(marks_list), 2)
    status = "Pass" if avg >= 60 else "Fail"

    all_averages.append(avg)

    # Count pass/fail
    if status == "Pass":
        passed += 1
    else:
        failed += 1

    # Track topper
    if avg > topper_avg:
        topper_avg  = avg
        topper_name = name

    print(f"{name:<18}| {avg:^8}| {status}")

# Summary after table
class_average = round(sum(all_averages) / len(all_averages), 2)

print("-" * 40)
print(f"\nStudents Passed : {passed}")
print(f"Students Failed : {failed}")
print(f"Class Topper    : {topper_name} ({topper_avg})")
print(f"Class Average   : {class_average}")


# ============================================================
# Task 4 — String Manipulation Utility (5 marks)
# ============================================================

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip leading/trailing whitespace
clean_essay = essay.strip()
print(f"\nStep 1 - Stripped Essay:\n{clean_essay}")

# Step 2: Title Case
print(f"\nStep 2 - Title Case:\n{clean_essay.title()}")

# Step 3: Count occurrences of "python" (case-insensitive)
# clean_essay is already lowercase after strip, so direct count works
python_count = clean_essay.count("python")
print(f"\nStep 3 - 'python' appears: {python_count} time(s)")

# Step 4: Replace "python" with "Python 🐍"
replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"\nStep 4 - Replaced:\n{replaced_essay}")

# Step 5: Split into sentences on ". "
sentences = clean_essay.split(". ")
print(f"\nStep 5 - Sentences List:\n{sentences}")

# Step 6: Print each sentence numbered, ensure it ends with "."
print("\nStep 6 - Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    # Add "." at end if not already present
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")
