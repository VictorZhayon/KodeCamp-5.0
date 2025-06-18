
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")

def view_history(history):
    if not history:
        print("No history available.")
    else:
        print("\nHistory:")
        for index, entry in enumerate(history, start=1):
            print(f"{index}. {entry}")
    print()

def main():
    print("Welcome to the Calculator with History!")
    # History list to store operations and results
    history = []
    while True:
        print("Calculator Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == "6":
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "1":
                    result = add(num1, num2)
                    operation = f"{num1} + {num2} = {result}"
                elif choice == "2":
                    result = subtract(num1, num2)
                    operation = f"{num1} - {num2} = {result}"
                elif choice == "3":
                    result = multiply(num1, num2)
                    operation = f"{num1} * {num2} = {result}"
                elif choice == "4":
                    result = divide(num1, num2)
                    operation = f"{num1} / {num2} = {result}"
                
                history.append(operation)
                print(f"Result: {result}\n")
            except ValueError as e:
                print(f"Error: {e}\n")
        elif choice == "5":
            view_history(history)
        else:
            print("Invalid option. Please try again.\n")

main()