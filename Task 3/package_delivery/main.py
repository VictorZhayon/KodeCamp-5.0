import uuid
from delivery_utils import load_packages, save_packages

class Package:
    def __init__(self, sender, recipient, status="In Transit"):
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "sender": self.sender,
            "recipient": self.recipient,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        pkg = Package(data["sender"], data["recipient"], data["status"])
        pkg.id = data["id"]
        return pkg


class DeliverySystem:
    def __init__(self):
        self.packages = [Package.from_dict(p) for p in load_packages()]

    def register_package(self, sender, recipient):
        package = Package(sender, recipient)
        self.packages.append(package)
        print(f"Package registered. ID: {package.id}")

    def mark_delivered(self, pkg_id):
        for package in self.packages:
            if package.id == pkg_id:
                if package.status == "Delivered":
                    print("Package already delivered.")
                else:
                    package.status = "Delivered"
                    print("Package marked as delivered.")
                return
        print("Package ID not found.")

    def view_packages(self):
        if not self.packages:
            print("No packages registered.")
        for p in self.packages:
            print(f"ID: {p.id} | From: {p.sender} | To: {p.recipient} | Status: {p.status}")

    def save(self):
        save_packages([p.to_dict() for p in self.packages])
        print("Data saved.")


def menu():
    system = DeliverySystem()
    while True:
        print("\n=== Package Delivery Menu ===")
        print("1. Register a package")
        print("2. Mark package as delivered")
        print("3. View all packages")
        print("4. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            sender = input("Sender name: ")
            recipient = input("Recipient name: ")
            system.register_package(sender, recipient)
        elif choice == "2":
            pkg_id = input("Enter Package ID: ")
            system.mark_delivered(pkg_id)
        elif choice == "3":
            system.view_packages()
        elif choice == "4":
            system.save()
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
