print("Welcome to the Student Management System!")

# function to add a student
def add_student(students):
    try:
        name = input("Enter student name: ")
        if not name:
            print("Name cannot be empty.")
            return
        # List to store scores
        scores = []
        for i in range(1, 4):
            while True:
                try:
                    score = float(input(f"Enter score for subject {i}: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        students[name] = scores
        print(f"Student '{name}' added successfully!\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def show_students(students):
    if not students:
        print("No students to show.\n")
        return
    print("\nAll Students:")
    print("----------------------------------")
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        if avg >= 70:
            status = "Excellent"
        elif avg >= 50:
            status = "Good"
        else:
            status = "Fail. Needs Improvement"
        print(f"Name: {name}")
        print(f"Scores: {scores}")
        print(f"Average: {avg}")
        print(f"Performance: {status}")
        print("----------------------------------")
    print()

def search_student(students):
    name = input("Enter student name to search: ")
    if name in students:
        scores = students[name]
        avg = sum(scores) / len(scores)
        print(f"\nName: {name}")
        print(f"Scores: {scores}")
        print(f"Average: {avg}\n")
    else:
        print("Student not found.\n")

def main():
    students = {}
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.\n")

# Start the program
main()