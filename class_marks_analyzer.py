def get_positive_student_count():
    # Ask for a whole-number student count greater than zero.
    while True:
        try:
            count = int(input("How many students are in the class? "))

            if count > 0:
                return count

            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_mark(student_name):
    # Ask for one student's mark until it is an integer from 0 to 100.
    while True:
        try:
            mark = int(input(f"Enter marks for {student_name} (0-100): "))

            if 0 <= mark <= 100:
                return mark

            print("Invalid marks. Enter a value from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_name():
    # Return a student's name without leading or trailing spaces.
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name.title()

        print("Name cannot be empty. Please try again.")


def display_students_above_average(student_names, student_marks, average):
    # Display each student whose mark is strictly greater than the class average.
    print("\nSTUDENTS ABOVE CLASS AVERAGE")
    found_student = False

    for index in range(len(student_marks)):
        if student_marks[index] > average:
            print(f"{student_names[index]}: {student_marks[index]}")
            found_student = True

    if not found_student:
        print("No students scored above the class average.")


def display_sorted_results(student_names, student_marks):
    # Sort mark-and-name pairs by marks from highest to lowest.
    print("\nSTUDENT MARKS (HIGHEST TO LOWEST)")

    sorted_results = sorted(
        zip(student_marks, student_names),
        reverse=True
    )

    for mark, name in sorted_results:
        print(f"{name}: {mark}")


def main():
    # Collect class data and display the requested performance statistics.
    print("=" * 45)
    print("             CLASS MARKS ANALYZER")
    print("=" * 45)

    student_names = []
    student_marks = []

    student_count = get_positive_student_count()

    # Store each student's name and matching mark at the same list index.
    for student_number in range(1, student_count + 1):
        print(f"\nStudent {student_number}")
        name = get_valid_name()
        mark = get_valid_mark(name)

        student_names.append(name)
        student_marks.append(mark)

    # Calculate basic class statistics using built-in list functions.
    class_total = sum(student_marks)
    class_average = class_total / len(student_marks)
    highest_mark = max(student_marks)
    lowest_mark = min(student_marks)

    passing_count = 0
    failing_count = 0

    # Count passes and fails. A mark of exactly 50 is a pass.
    for mark in student_marks:
        if mark >= 50:
            passing_count += 1
        else:
            failing_count += 1

    print("\n" + "=" * 45)
    print("              CLASS SUMMARY")
    print("=" * 45)
    print(f"Number of Students : {len(student_names)}")
    print(f"Class Average      : {class_average:.2f}")
    print(f"Highest Marks      : {highest_mark}")
    print(f"Lowest Marks       : {lowest_mark}")
    print(f"Passing Students  : {passing_count}")
    print(f"Failing Students  : {failing_count}")

    # Show every student tied for the highest mark.
    print("\nHIGHEST-SCORING STUDENT(S)")
    for index in range(len(student_marks)):
        if student_marks[index] == highest_mark:
            print(f"{student_names[index]}: {student_marks[index]}")

    # Show every student tied for the lowest mark.
    print("\nLOWEST-SCORING STUDENT(S)")
    for index in range(len(student_marks)):
        if student_marks[index] == lowest_mark:
            print(f"{student_names[index]}: {student_marks[index]}")

    display_students_above_average(
        student_names, student_marks, class_average
    )
    display_sorted_results(student_names, student_marks)

    print("\n" + "=" * 45)
    print("Analysis completed successfully.")
    print("=" * 45)


if __name__ == "__main__":
    main()
