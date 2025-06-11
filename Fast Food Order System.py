# Prices of each item
burger_price = 5.0
fries_price = 2.0
drink_price = 1.5

# Count of customers served
customer_count = 0

print("=== Task 2: Fast Food Order System ===")

while True:
    print("\n--- New Customer ---")
    
    name = input("Enter your name (or type 'exit' to finish): ")

    # Check if the user wants to exit
    if name.lower() == 'exit':
        break

    # Ask for quantities of each item
    burgers = int(input("How many burgers would you like? ($5 each): "))
    fries = int(input("How many fries would you like? ($2 each): "))
    drinks = int(input("How many drinks would you like? ($1.5 each): "))

    # Calculate total cost
    total = (burgers * burger_price) + (fries * fries_price) + (drinks * drink_price)

    # Apply 10% discount if total is more than $20
    if total > 20:
        discount = total * 0.10
        total = total - discount
        print("You got a 10% discount!")

    # Display the bill
    print("\n--- Bill for", name, "---")
    print("Burgers:", burgers, "x $5 =", burgers * burger_price)
    print("Fries:", fries, "x $2 =", fries * fries_price)
    print("Drinks:", drinks, "x $1.5 =", drinks * drink_price)
    print("Total to pay: $", round(total, 2))

    # Increase customer count
    customer_count += 1

# After all customers are served
print("\nTotal customers served:", customer_count)
