<div align="center">

<img src="assets/header.svg" alt="Python Functions, Strings, Lists and Tuples: animated banner" width="100%">

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-d97757?style=for-the-badge&logo=python&logoColor=white&labelColor=14161d)
![Topics](https://img.shields.io/badge/Topics-4-ff4d8d?style=for-the-badge&labelColor=14161d)
![Challenges](https://img.shields.io/badge/Challenges-19-3ddc97?style=for-the-badge&labelColor=14161d)
![Dependencies](https://img.shields.io/badge/Dependencies-none-6c5ce7?style=for-the-badge&labelColor=14161d)

### 🔗 [Open the visual preview &rarr;](./preview.html)

<sub>GitHub shows `preview.html` as source code. To see it rendered, enable **GitHub Pages** (Settings &rarr; Pages &rarr; deploy from branch) and open<br>`https://<your-username>.github.io/<repo-name>/preview.html`, or just open the file in your browser after cloning.</sub>

</div>

---

# Python Functions, Strings, Lists & Tuples

## Learning Path

<img src="assets/learning-path.svg" alt="Learning path from functions, strings, lists and tuples to OOP, Django, REST APIs and AI apps" width="100%">

## Repository Structure
```text
python-functions-and-strings/
├── README.md
├── preview.html
├── 01_functions_fundamentals.py
├── 02_strings_lists_tuples.py
└── assets/
    ├── header.svg
    ├── footer.svg
    ├── learning-path.svg
    ├── function-flow.svg
    ├── print-vs-return.svg
    ├── string-slicing.svg
    ├── collections-matrix.svg
    ├── challenges-chart.svg
    └── er-diagram.svg
```

All graphics are animated vector SVGs, so they stay sharp at any resolution, including HD and retina displays.

## Lecture Files

| File | Concepts |
|---|---|
| `01_functions_fundamentals.py` | Function definition and calls, parameters, arguments, defaults, `print()` vs `return`, scope, `*args`, `**kwargs`, validation, reusable function design |
| `02_strings_lists_tuples.py` | Quotes, indexing, slicing, immutability, f-string formatting, string cleaning, `split()` and `join()`, lists, list methods, list comprehension, tuples, unpacking |
| `preview.html` | Visual, animated overview of this lecture. Open it in any browser |

## Requirements
- Python 3.10 or later
- VS Code or another Python editor
- Terminal / Command Prompt
- No third-party packages required

## Key Concepts

### Functions
Functions organize code into reusable blocks. Parameters receive information; `return` sends a result back to the caller.

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

bill = calculate_total(250, 3)
print(bill)
```

<img src="assets/function-flow.svg" alt="How a function call works: arguments in, return value out" width="100%">

### `print()` vs `return`

| `print()` | `return` |
|---|---|
| Displays information on the screen | Sends a value back to the caller |
| Useful for messages and output | Useful when a result must be stored, reused, or tested |

<img src="assets/print-vs-return.svg" alt="print shows a value and loses it; return hands it back" width="100%">

### Strings

Strings store text. They support indexing and slicing, but are immutable: individual characters cannot be changed in place. Create a new string when modifying text.

<img src="assets/string-slicing.svg" alt="Indexing and slicing of the string PYTHON" width="100%">

### Lists

Lists are ordered, mutable collections. Use methods such as `append()`, `insert()`, `remove()`, and `pop()` to manage items.

### Tuples

Tuples are ordered, immutable collections. They are useful for fixed records and support unpacking into variables.

### Choosing a Data Structure

<img src="assets/collections-matrix.svg" alt="Capability matrix comparing str, list and tuple" width="100%">

## Data Model Behind the Challenges

The student, marks, expense and shopping-bill challenges all describe the same small data model. In Python, one tuple inside a list is one row of a table.

<img src="assets/er-diagram.svg" alt="ER diagram with STUDENT, SUBJECT, MARK, EXPENSE, BILL and BILL_ITEM" width="100%">

<details>
<summary>Same diagram as Mermaid (renders natively on GitHub)</summary>

```mermaid
erDiagram
    STUDENT ||--o{ MARK : earns
    SUBJECT ||--o{ MARK : has
    STUDENT ||--o{ EXPENSE : records
    STUDENT ||--o{ BILL : receives
    BILL ||--o{ BILL_ITEM : lists

    STUDENT {
        int student_id PK
        str full_name
        str email
        str phone
    }
    SUBJECT {
        int subject_id PK
        str name
        int total_marks
    }
    MARK {
        int mark_id PK
        int student_id FK
        int subject_id FK
        int score
    }
    EXPENSE {
        int expense_id PK
        int student_id FK
        str label
        float amount
    }
    BILL {
        int bill_id PK
        int student_id FK
        int discount_pct
    }
    BILL_ITEM {
        int item_id PK
        int bill_id FK
        str name
        float price
        int qty
    }
```

</details>

## Student Practice Challenges

<img src="assets/challenges-chart.svg" alt="Bar chart and donut showing 19 challenges: Functions 5, Strings 5, Lists 4, Tuples 5" width="100%">

### Functions

1. Write a function to calculate the area of a rectangle.
2. Calculate a student's percentage out of 1100 marks.
3. Create a shopping-bill function that applies a 10% discount.
4. Accept multiple expense values using `*args`.
5. Create a student profile function using `**kwargs`.

### Strings

1. Ask for a full name and remove unnecessary spaces.
2. Convert an email address to lowercase.
3. Extract the first four characters of a string.
4. Reverse a student's name using slicing.
5. Format a Pakistani phone number as `+92 300 1234567`.

### Lists

1. Create a list of five student names.
2. Add, update, and remove names.
3. Store five examination marks and calculate their average.
4. Display marks greater than or equal to 80.

### Tuples

1. Create a tuple containing student information.
2. Access tuple values using indexing.
3. Unpack a tuple into separate variables.
4. Explain why a tuple cannot be modified.
5. Store multiple student records using tuples inside a list.

## GitHub Submission Instructions

1. Clone this repository.
2. Run both Python files.
3. Review and understand the examples.
4. Complete the practice challenges in your own Python file(s).
5. Push your work to your own GitHub repository.
6. Submit your repository URL for assessment.

## Key Takeaways

- **Functions** make code reusable and organized.
- **Strings** represent and transform textual information.
- **Lists** manage collections that can change.
- **Tuples** store ordered data that should remain fixed.

These fundamentals prepare students for Python OOP, Django, REST APIs, and AI-powered applications.

---

<img src="assets/footer.svg" alt="PSEB DEPLOY: Python, Django and AI Bootcamp. Instructor Waleed Shehbaz" width="100%">

<div align="center">

**PSEB DEPLOY: Python, Django & AI Bootcamp**  
Author: [Maida Javed]

</div>
