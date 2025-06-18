
# Function to add expense
def add_expense(expenses):
    try:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        expenses.append({"item": description, "amount": amount})
        print(f"Expense '{description}' added successfully!\n")
    except:
        print(f"Invalid input. Please enter a valid description and amount.\n")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("\nAll Expenses:")
    print("----------------------------------")
    for expense in expenses:
        print(f"Item: {expense['item']}, Amount: {expense['amount']}")
    print("----------------------------------\n")

# Function to calculate total and average expenses
def total_and_average(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return
    # Calculate total expenses in the expenses dictionary
    total = sum(expense['amount'] for expense in expenses)
    # Calculate the average expense in the expenses dictionary
    average = total / len(expenses)
    print(f"Total Expenses: {total}")
    print(f"Average Expense: {average}\n")
    
def main():
    expenses = []
    while True:
        print("Simple Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total and Average Expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_and_average(expenses)
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()