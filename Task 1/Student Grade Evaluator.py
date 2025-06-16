print("=== Task 1: Student Grade Evaluator ===")
num_students = int(input("How many students do you want to process? "))

# Initialize counters for the summary
passed = 0
failed = 0
excellent = 0

# Loop through each student
for i in range(num_students):
    print("\n--- Student", i + 1, "---")
    
    # Get the student's name
    name = input("Enter the student's name: ")

    # Get 3 subject scores
    score1 = float(input("Enter score for subject 1: "))
    score2 = float(input("Enter score for subject 2: "))
    score3 = float(input("Enter score for subject 3: "))

    # Calculate the average score
    average = (score1 + score2 + score3) / 3

    # Determine the result
    if average < 50:
        result = "Fail"
        failed = failed + 1
    elif average >= 50 and average <= 79:
        result = "Pass"
        passed = passed + 1
    else:
        result = "Excellent"
        excellent = excellent + 1

    # Show the result for the student
    print(name + "'s average score is", round(average, 2), "- Result:", result)

# After all students are processed, show the summary
print("\n--- Summary ---")
print("Number of students who passed:", passed)
print("Number of students who failed:", failed)
print("Number of students who did excellent:", excellent)
