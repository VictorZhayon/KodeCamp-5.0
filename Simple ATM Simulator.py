print("=== Task 5: Simple ATM Simulator ===")
# Starting account balance
balance = 1000.0

print("Welcome to the Simple ATM!")

while True:
    # Show menu
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Ask user for their choice
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Check balance
        print("Your current balance is: $", round(balance, 2))

    elif choice == '2':
        # Deposit money
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposit successful! New balance: $", round(balance, 2))
        else:
            print("Invalid amount! Deposit must be greater than zero.")

    elif choice == '3':
        # Withdraw money
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds! Your balance is only $", round(balance, 2))
        elif amount <= 0:
            print("Invalid amount! Withdrawal must be greater than zero.")
        else:
            balance -= amount
            print("Withdrawal successful! New balance: $", round(balance, 2))

    elif choice == '4':
        # Exit the ATM
        print("\nThank you for using the Simple ATM.")
        print("Your final balance is: $", round(balance, 2))
        break

    else:
        print("Invalid choice! Please select option 1, 2, 3, or 4.")
