from library_utils import load_books, save_books

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {"title": self.title, "author": self.author, "available": self.available}

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["available"])


class Library:
    def __init__(self):
        self.books = [Book.from_dict(b) for b in load_books()]

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f'Book "{title}" by {author} added.')

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f'You borrowed "{book.title}".')
                return
        print("Book not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f'You returned "{book.title}".')
                return
        print("Book not found or already returned.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f'{book.title} by {book.author} - {status}')

    def save(self):
        save_books([b.to_dict() for b in self.books])
        print("Library saved successfully.")


def menu():
    library = Library()
    while True:
        print("\n=== Library Menu ===")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View all books")
        print("5. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)
        elif choice == "2":
            title = input("Enter title to borrow: ")
            library.borrow_book(title)
        elif choice == "3":
            title = input("Enter title to return: ")
            library.return_book(title)
        elif choice == "4":
            library.view_books()
        elif choice == "5":
            library.save()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
