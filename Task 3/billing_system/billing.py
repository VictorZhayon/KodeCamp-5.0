import json
import os
from datetime import datetime
import math

DATA_FILE = "billing_system/transactions.json"

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_price(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "total": self.total_price()
        }

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        try:
            price = float(price)
            quantity = int(quantity)
            self.products.append(Product(name, price, quantity))
            print("Product added to cart.")
        except ValueError:
            print("Invalid price or quantity.")

    def view_cart(self):
        if not self.products:
            print("Cart is empty.")
        for p in self.products:
            print(f"{p.name} - ₦{p.price} x {p.quantity} = ₦{p.total_price()}")

    def calculate_total(self):
        total = sum(p.total_price() for p in self.products)
        if total > 10000:
            discount = 0.10 * total
            total -= discount
            print(f"Discount applied: ₦{discount:.2f}")
        return math.ceil(total)

    def save_transaction(self):
        if not self.products:
            print("Cart is empty. Nothing to save.")
            return

        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": [p.to_dict() for p in self.products],
            "total": self.calculate_total()
        }

        transactions = []
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                try:
                    transactions = json.load(f)
                except json.JSONDecodeError:
                    pass

        transactions.append(entry)

        with open(DATA_FILE, "w") as f:
            json.dump(transactions, f, indent=4)
        print("Transaction saved.")

    def reset_cart(self):
        self.products = []

def view_previous_transactions():
    if not os.path.exists(DATA_FILE):
        print("No previous transactions.")
        return

    with open(DATA_FILE, "r") as f:
        try:
            transactions = json.load(f)
        except json.JSONDecodeError:
            transactions = []

    for tx in transactions:
        print(f'\nDate: {tx["timestamp"]}')
        for item in tx["items"]:
            print(f'{item["name"]} - ₦{item["price"]} x {item["quantity"]} = ₦{item["total"]}')
        print(f'Total: ₦{tx["total"]}')
