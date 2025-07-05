from billing import Cart, view_previous_transactions

def menu():
    cart = Cart()

    while True:
        print("\n=== Billing System Menu ===")
        print("1. Add product to cart")
        print("2. View cart and total")
        print("3. Apply discount and save bill")
        print("4. View previous transactions")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Product name: ")
            price = input("Price: ")
            quantity = input("Quantity: ")
            cart.add_product(name, price, quantity)

        elif choice == "2":
            cart.view_cart()
            total = cart.calculate_total()
            print(f"Total (after any discount): ₦{total}")

        elif choice == "3":
            cart.save_transaction()
            cart.reset_cart()

        elif choice == "4":
            view_previous_transactions()

        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
