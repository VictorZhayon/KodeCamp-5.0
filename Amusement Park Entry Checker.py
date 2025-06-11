print("=== Task 3: Amusement Park Entry Checker ===")
print("Welcome to the Amusement Park!")
print("Type 'exit' as name when you're finished.\n")

while True:
    # Ask for visitor's name
    name = input("Enter visitor's name: ")

    # Check if user wants to stop
    if name.lower() == 'exit':
        break

    # Ask for age
    age = int(input("Enter age: "))

    # Determine base ticket price
    if age < 5:
        price = 0
    elif age >= 5 and age <= 17:
        price = 5
    elif age >= 18 and age <= 59:
        price = 10
    else:  # age >= 60
        price = 7

    # Ask if they have a coupon
    has_coupon = input("Do you have a coupon? (Yes/No): ")

    # Apply 20% discount if they have a coupon
    if has_coupon.lower() == 'yes' and price > 0:
        discount = price * 0.20
        price = price - discount

    # Show final price
    print(name + "'s ticket price is: $" + str(round(price, 2)) + "\n")

print("All visitors have been processed. Have a great day!")
