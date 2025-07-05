import json
import os

DATA_FILE = "package_delivery/packages.json"

def load_packages():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_packages(packages):
    with open(DATA_FILE, "w") as f:
        json.dump(packages, f, indent=4)
