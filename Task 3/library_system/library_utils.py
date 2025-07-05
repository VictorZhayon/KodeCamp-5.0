import json
import os

DATA_FILE = "library_system/books.json"

def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)
