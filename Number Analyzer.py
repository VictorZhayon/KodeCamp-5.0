print("=== Task 4: Number Analyzer ===")
print("Welcome to the Number Analyzer!")
print("You can enter up to 5 numbers.\n")

# Counters
even_count = 0
odd_count = 0
negative_count = 0
zero_count = 0

# Loop to enter 5 numbers
for i in range(5):
    number = int(input("Enter number " + str(i + 1) + ": "))

    # Check if even or odd
    if number % 2 == 0:
        print("This number is even.")
        even_count += 1
    else:
        print("This number is odd.")
        odd_count += 1

    # Check if positive, negative, or zero
    if number > 0:
        print("It is positive.\n")
    elif number < 0:
        print("It is negative.\n")
        negative_count += 1
    else:
        print("It is zero.\n")
        zero_count += 1

# Final summary
print("--- Summary ---")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
