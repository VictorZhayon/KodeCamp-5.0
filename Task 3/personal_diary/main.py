from datetime import datetime
from diary_tools import load_entries, save_entries, search_entries

class DiaryEntry:
    def __init__(self, title, content):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.title = title
        self.content = content

    def to_dict(self):
        return {"date": self.date, "title": self.title, "content": self.content}

    @staticmethod
    def from_dict(data):
        entry = DiaryEntry(data["title"], data["content"])
        entry.date = data["date"]
        return entry


class Diary:
    def __init__(self):
        self.entries = [DiaryEntry.from_dict(e) for e in load_entries()]

    def add_entry(self, title, content):
        entry = DiaryEntry(title, content)
        self.entries.append(entry)
        print("Entry added.")

    def view_entries(self):
        if not self.entries:
            print("No entries found.")
        for entry in self.entries:
            print(f'\n[{entry.date}] {entry.title}\n{entry.content}\n')

    def search(self, keyword):
        results = search_entries([e.to_dict() for e in self.entries], keyword)
        if not results:
            print("No matching entries found.")
        for entry in results:
            print(f'\n[{entry["date"]}] {entry["title"]}\n{entry["content"]}\n')

    def save(self):
        save_entries([e.to_dict() for e in self.entries])
        print("Diary saved.")


def menu():
    diary = Diary()
    while True:
        print("\n=== Personal Diary Menu ===")
        print("1. Add entry")
        print("2. View all entries")
        print("3. Search by date or title")
        print("4. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            diary.add_entry(title, content)
        elif choice == "2":
            diary.view_entries()
        elif choice == "3":
            keyword = input("Enter title or date to search: ")
            diary.search(keyword)
        elif choice == "4":
            diary.save()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
