# Python Functions, Strings and Lists Assessment

## Project Overview

This repository contains two beginner-friendly Python programs developed for the **Functions, Strings and Lists Assessment**. The programs demonstrate how to collect user input, validate data, organize information, use custom functions, and present clear results.

Both tasks are independent and are saved in separate Python files.

## Project Structure

```text
python-functions-lists-assessment/
│
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

## Task 1: Student Result Card Generator

### Purpose

The Student Result Card Generator collects one student's name, roll number, and marks in five subjects. It calculates the total marks, percentage, and letter grade, then displays a neatly formatted result card.

### Main Features

- Collects the student's name and roll number.
- Collects marks in English, Mathematics, Science, Computer, and Urdu.
- Accepts marks only when they are whole numbers from 0 to 100.
- Checks that the roll number contains digits only.
- Cleans the student's name by removing extra spaces and applying title case.
- Calculates the percentage and assigns a grade.
- Applies the special rule that a mark below 40 in any subject makes the final status **Fail**.
- Displays the result using formatted strings.

### Functions Used

| Function | Purpose |
|---|---|
| `get_valid_marks(subject)` | Repeatedly asks for marks until a valid value from 0 to 100 is entered. |
| `get_valid_roll_number()` | Accepts a roll number containing digits only. |
| `get_valid_name()` | Ensures the student name is not empty. |
| `format_name(name)` | Removes extra spaces and converts the name to title case. |
| `calculate_percentage(total, max_total)` | Calculates the student's percentage. |
| `get_grade(percentage)` | Returns the letter grade according to the grading scale. |
| `main()` | Controls the program from input collection to result-card display. |

### Grading Criteria

| Percentage | Grade |
|---|---|
| 90% and above | A+ |
| 80% to below 90% | A |
| 70% to below 80% | B |
| 60% to below 70% | C |
| 50% to below 60% | D |
| Below 50% | Fail |

**Important result rule:** If any individual subject mark is below 40, the final status is `Fail`, even if the overall percentage is 50% or higher. The letter grade is calculated from the overall percentage; the final status also considers the individual-subject rule.

### Logic Explained Step by Step

1. The program asks for the student's name. It removes extra spaces and formats the name.
2. It asks for the roll number. The `.isdigit()` method checks that the entered value contains digits only.
3. A loop visits the five subject names. For each subject, `get_valid_marks()` keeps asking until the input is a valid integer between 0 and 100.
4. `sum()` adds all five marks. The maximum possible total is `5 * 100`, which is 500.
5. `calculate_percentage()` divides the obtained total by the maximum total and multiplies by 100.
6. `get_grade()` checks the percentage from the highest grade range to the lowest.
7. `any()` checks whether at least one subject mark is below 40. If so, the final status is `Fail`; otherwise, a percentage of at least 50 gives `Pass`.
8. The program prints the student's information, subject marks, total, percentage, grade, and final status.

### Python Concepts Used

- Defining and calling functions with `def`.
- Function parameters and `return`.
- `input()` and type conversion with `int()`.
- `try` and `except` for invalid numeric input.
- `while` and `for` loops.
- Conditional statements: `if`, `elif`, and `else`.
- String methods: `.strip()`, `.title()`, and `.isdigit()`.
- Dictionary storage for subject names and marks.
- Built-in functions: `sum()`, `len()`, and `any()`.
- F-strings and number formatting with `:.2f`.

### Sample Run

**Sample input** (entered by the user):

```text
Student name:   ali ahmed
Roll number: 1025
English: 85
Mathematics: 92
Science: 78
Computer: 88
Urdu: 80
```

**Sample output:**

```text
=============================================
                 RESULT CARD
=============================================
Student Name       : Ali Ahmed
Roll Number        : 1025
---------------------------------------------
SUBJECTS AND MARKS
English             :  85/100
Mathematics         :  92/100
Science             :  78/100
Computer            :  88/100
Urdu                :  80/100
---------------------------------------------
Total Marks        : 423/500
Percentage         : 84.60%
Letter Grade       : A
Final Status       : Pass
=============================================
```

## Task 2: Class Marks Analyzer

### Purpose

The Class Marks Analyzer collects the names and marks of all students in a class. It uses two separate lists to store the data and then calculates useful class statistics.

### Main Features

- Asks how many students are in the class.
- Stores names in `student_names` and marks in `student_marks`.
- Uses `.append()` to add each student's information.
- Validates every mark so it is a whole number from 0 to 100.
- Calculates the class average, highest mark, and lowest mark.
- Displays all students tied for the highest and lowest marks.
- Counts passing students (50 or above) and failing students (below 50).
- Displays students whose marks are strictly above the class average.
- Displays student marks from highest to lowest.

### Functions Used

| Function | Purpose |
|---|---|
| `get_positive_student_count()` | Keeps asking until the user enters a positive whole number. |
| `get_valid_mark(student_name)` | Validates one student's mark. |
| `get_valid_name()` | Ensures a student name is not empty and formats it. |
| `display_students_above_average(...)` | Displays students whose marks are above the class average. |
| `display_sorted_results(...)` | Displays student names and marks in descending mark order. |
| `main()` | Collects class information and coordinates the analysis. |

### Logic Explained Step by Step

1. The program creates two empty lists: `student_names` and `student_marks`.
2. It asks for the number of students. The program accepts only a positive whole number.
3. A `for` loop runs once for each student.
4. During each loop, the program gets a student's name and a valid mark. It stores both values using `.append()`.
5. The name and mark are stored at matching list positions. For example, `student_names[0]` belongs to `student_marks[0]`.
6. `sum(student_marks)` calculates the total marks. Dividing this total by `len(student_marks)` gives the class average.
7. `max()` and `min()` find the highest and lowest marks.
8. A loop counts passing students (50 or more) and failing students (below 50).
9. Another loop compares each mark with the highest and lowest marks. This displays every student who shares either result, including ties.
10. `display_students_above_average()` prints students whose marks are greater than the average. A mark equal to the average is not included.
11. `zip()` pairs each mark with its student's name. `sorted(..., reverse=True)` arranges these pairs from highest to lowest marks.

### Python Concepts Used

- Creating and using lists.
- `.append()` to add values.
- `len()`, `sum()`, `max()`, and `min()`.
- `sorted()` with `reverse=True`.
- `zip()` to keep each student's name paired with their mark.
- `for` and `while` loops.
- `if` and `else` conditions.
- Custom functions, parameters, and return values.
- Input validation using `try` and `except`.
- F-strings for readable output.

### Sample Run

**Sample input** (entered by the user):

```text
Number of students: 4

Student name: Ali
Marks: 85

Student name: Sara
Marks: 92

Student name: Hamza
Marks: 45

Student name: Ayesha
Marks: 78
```

**Sample output:**

```text
=============================================
              CLASS SUMMARY
=============================================
Number of Students : 4
Class Average      : 75.00
Highest Marks      : 92
Lowest Marks       : 45
Passing Students  : 3
Failing Students  : 1

HIGHEST-SCORING STUDENT(S)
Sara: 92

LOWEST-SCORING STUDENT(S)
Hamza: 45

STUDENTS ABOVE CLASS AVERAGE
Ali: 85
Sara: 92
Ayesha: 78

STUDENT MARKS (HIGHEST TO LOWEST)
Sara: 92
Ali: 85
Ayesha: 78
Hamza: 45
```

## How to Run the Programs

### Requirements

- Python 3.8 or later.
- A code editor or terminal, such as VS Code, IDLE, or Command Prompt.

No external Python packages are required.

### Step 1: Get the Project

Clone the repository:

```bash
git clone https://github.com/your-username/python-functions-lists-assessment.git
```

Move into the project folder:

```bash
cd python-functions-lists-assessment
```

### Step 2: Run Task 1

```bash
python result_card_generator.py
```

If your system uses the `python3` command, run:

```bash
python3 result_card_generator.py
```

### Step 3: Run Task 2

```bash
python class_marks_analyzer.py
```

Or:

```bash
python3 class_marks_analyzer.py
```

Run each command separately. The programs are independent.

## Input Validation and Testing

The programs are designed to handle common invalid inputs:

| Test case | Expected behavior |
|---|---|
| Marks contain letters, such as `abc` | Display an error and ask again. |
| Marks are below 0 or above 100 | Display an error and ask again. |
| Roll number contains letters or symbols | Ask for a digits-only roll number again. |
| Student name is empty or contains only spaces | Ask for the name again. |
| Class size is zero or negative | Ask for a positive student count again. |
| One subject mark is below 40 in Task 1 | Final result status is `Fail`. |
| Two or more students share the highest or lowest mark in Task 2 | Display every student who shares that mark. |
| A student's mark equals the class average in Task 2 | Do not include that student in the above-average list. |

## GitHub Submission

After placing the three files in the project folder, use the following commands to upload the project:

```bash
git init
git add result_card_generator.py class_marks_analyzer.py README.md
git commit -m "Complete functions and lists assessment"
git branch -M main
git remote add origin https://github.com/your-username/python-functions-lists-assessment.git
git push -u origin main
```

Replace `your-username` with your actual GitHub username. If the repository already exists locally or the remote has already been added, do not repeat the corresponding setup command.

## Final Checklist

- [ ] Both Python programs are saved in separate files.
- [ ] Every required function is included.
- [ ] Input validation works for invalid entries.
- [ ] Both programs have been tested with different input values.
- [ ] The README file is included in the repository.
- [ ] All three files have been pushed to GitHub.
- [ ] The repository URL and required files are submitted to the LMS.

## Conclusion

This project demonstrates the practical use of Python functions, string methods, lists, loops, conditional statements, and input validation. The first program generates an individual student's result card, while the second program analyzes the performance of an entire class.
