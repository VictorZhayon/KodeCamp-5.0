import json
import os

DATA_FILE = "personal_diary/diary_entries.json"

def load_entries():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_entries(entries):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(entries, f, indent=4)
    except IOError:
        print("Error saving entries.")

def search_entries(entries, keyword):
    results = []
    for entry in entries:
        if keyword.lower() in entry["title"].lower() or keyword in entry["date"]:
            results.append(entry)
    return results
