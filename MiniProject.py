students = []
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
def add_student():
    name = input("Student name: ")
    scores = []

    while True:
        score = input("Enter score or 'done': ")

        if score.lower() == "done":
            break

        try:
            score = float(score)

            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input.")

    avg = calculate_average(scores)
    grade = get_letter_grade(avg)

    students.append({
        "name": name,
        "scores": scores,
        "average": avg,
        "grade": grade
    })

    print(f"Added {name} - Average: {avg:.2f} - Grade: {grade}")

# Function to view all students
def view_students():
    if not students:
        print("No students available.")
        return

    print("\nStudent Records:")
    for student in students:
        print(f"{student['name']} | Average: {student['average']:.2f} | Grade: {student['grade']}")

# Function to display class report
def show_class_report():
    if not students:
        print("No student data available.")
        return

    highest = max(students, key=lambda x: x["average"])
    lowest = min(students, key=lambda x: x["average"])

    class_avg = sum(student["average"] for student in students) / len(students)

    print("\n--- Class Report ---")
    print("Total Students:", len(students))
    print(f"Highest Average: {highest['name']} with {highest['average']:.2f}")
    print(f"Lowest Average: {lowest['name']} with {lowest['average']:.2f}")
    print(f"Class Average: {class_avg:.2f}")

# Main function
def main():
    while True:
        print("\n--- Grade Calculator ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Class Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            show_class_report()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


main()