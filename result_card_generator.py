# Store the five subject names in a list.
SUBJECTS = ["English", "Mathematics", "Science", "Computer", "Urdu"]
def get_valid_marks(subject):
    # Ask for a subject's marks until the user enters a whole number from 0 to 100.
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks. Enter a value from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_roll_number():
    # Accept a roll number only when it contains digits and is not empty.
    while True:
        roll_number = input("Enter roll number: ").strip()

        if roll_number.isdigit():
            return roll_number

        print("Invalid roll number. Use digits only (for example, 1025).")


def format_name(name):
    # Remove extra spaces and capitalize the first letter of each name part.
    return name.strip().title()


def calculate_percentage(total, max_total):
    # Convert obtained marks into a percentage.
    return (total / max_total) * 100


def get_grade(percentage):
    # Return the letter grade that matches the student's percentage.
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def get_valid_name():
    # Keep asking until the student enters a name containing non-space characters.
    while True:
        name = input("Enter student name: ")

        if name.strip():
            return format_name(name)

        print("Name cannot be empty. Please try again.")


def main():
    # Collect the student's information, calculate the result, and display the card.
    print("=" * 45)
    print("        STUDENT RESULT CARD GENERATOR")
    print("=" * 45)

    student_name = get_valid_name()
    roll_number = get_valid_roll_number()

    marks_by_subject = {}
    for subject in SUBJECTS:
        marks_by_subject[subject] = get_valid_marks(subject)

    total_marks = sum(marks_by_subject.values())
    maximum_marks = len(SUBJECTS) * 100
    percentage = calculate_percentage(total_marks, maximum_marks)
    grade = get_grade(percentage)

    # A mark below 40 in even one subject makes the final status Fail.
    if any(mark < 40 for mark in marks_by_subject.values()):
        final_status = "Fail"
    elif percentage >= 50:
        final_status = "Pass"
    else:
        final_status = "Fail"

    print("\n" + "=" * 45)
    print("                 RESULT CARD")
    print("=" * 45)
    print(f"Student Name       : {student_name}")
    print(f"Roll Number        : {roll_number}")
    print("-" * 45)
    print("SUBJECTS AND MARKS")

    for subject, marks in marks_by_subject.items():
        print(f"{subject:<20}: {marks:>3}/100")

    print("-" * 45)
    print(f"Total Marks        : {total_marks}/{maximum_marks}")
    print(f"Percentage         : {percentage:.2f}%")
    print(f"Letter Grade       : {grade}")
    print(f"Final Status       : {final_status}")
    print("=" * 45)


if __name__ == "__main__":
    main()
