
def show_items(store_items):
    print("\nAvailable Items:")
    print("-------------------------------")
    for item, price in store_items.items():
        print(f"{item}: ${price}")
    print("-------------------------------")

def add_to_cart(store_items, cart):
    item = input("Enter item name to add: ")
    if item not in store_items:
        print("Item not found in store.\n")
        return
    try:
        qty = int(input(f"Enter quantity for {item}: "))
        if qty <= 0:
            print("Quantity must be positive.\n")
            return
        # Check if item already in cart
        for entry in cart:
            if entry["item"] == item:
                entry["quantity"] += qty
                print(f"Updated {item} quantity in cart.\n")
                return
        cart.append({"item": item, "quantity": qty, "price": store_items[item]})
        print(f"Added {item} x{qty} to cart.\n")
    except ValueError:
        print("Invalid quantity. Please enter a number.\n")

def view_cart(cart):
    if not cart:
        print("Cart is empty.\n")
        return
    print("\nYour Cart:")
    print("-------------------------------")
    total = 0
    for entry in cart:
        subtotal = entry["quantity"] * entry["price"]
        print(f"{entry['item']} x{entry['quantity']} - ${entry['price']} each (Subtotal: ${subtotal})")
        total += subtotal
    print("-------------------------------")
    print(f"Total Bill: ${total}\n")

def remove_from_cart(cart):
    if not cart:
        print("Cart is empty.\n")
        return
    item = input("Enter item name to remove: ")
    for entry in cart:
        if entry["item"] == item:
            cart.remove(entry)
            print(f"Removed {item} from cart.\n")
            return
    print("Item not found in cart.\n")

def clear_cart(cart):
    cart.clear()
    print("Cart cleared.\n")

def main():
    store_items = {
        "Rice": 400,
        "Beans": 350,
        "Oil": 1000,
        "Bread": 500,
        "Milk": 250
    }
    cart = []
    while True:
        print("Shopping Cart System")
        print("1. Show Store Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove Item from Cart")
        print("5. Clear Cart")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            show_items(store_items)
        elif choice == "2":
            show_items(store_items)
            add_to_cart(store_items, cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            view_cart(cart)
            remove_from_cart(cart)
        elif choice == "5":
            clear_cart(cart)
        elif choice == "6":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please select 1-6.\n")

main()