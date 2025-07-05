from employee_utils import load_employees, save_employees, search_employee_by_id

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.id = emp_id
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "department": self.department,
            "salary": self.salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(data["name"], data["id"], data["department"], data["salary"])


class EmployeeManager:
    def __init__(self):
        self.employees = [Employee.from_dict(e) for e in load_employees()]

    def add_employee(self):
        name = input("Employee name: ")
        emp_id = input("Employee ID: ")
        department = input("Department: ")
        try:
            salary = float(input("Salary: "))
            emp = Employee(name, emp_id, department, salary)
            self.employees.append(emp)
            print("Employee added.")
        except ValueError:
            print("Invalid salary. Must be a number.")

    def view_all(self):
        if not self.employees:
            print("No employees found.")
            return
        for e in self.employees:
            print(f"{e.name} | ID: {e.id} | Dept: {e.department} | Salary: ₦{e.salary}")

    def search_by_id(self):
        emp_id = input("Enter Employee ID: ")
        found = search_employee_by_id([e.to_dict() for e in self.employees], emp_id)
        if found:
            print(f"Found: {found['name']} | Dept: {found['department']} | Salary: ₦{found['salary']}")
        else:
            print("Employee not found.")

    def save(self):
        save_employees([e.to_dict() for e in self.employees])
        print("Employees saved.")

    def load(self):
        self.employees = [Employee.from_dict(e) for e in load_employees()]
        print("Employees loaded.")


def menu():
    manager = EmployeeManager()

    while True:
        print("\n=== Employee Manager Menu ===")
        print("1. Add employee")
        print("2. View all employees")
        print("3. Search by ID")
        print("4. Save to file")
        print("5. Load from file")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            manager.search_by_id()
        elif choice == "4":
            manager.save()
        elif choice == "5":
            manager.load()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
