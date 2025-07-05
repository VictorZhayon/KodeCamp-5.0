import json
import os

DATA_FILE = "employee_manager/employees.json"

def load_employees():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_employees(employees):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(employees, f, indent=4)
    except IOError:
        print("Error saving employees.")

def search_employee_by_id(employees, emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    return None
