
# function to show available movies
def show_movies(movies):
    print("\nAvailable Movies:")
    print("-------------------------------")
    for name, info in movies.items():
        print(f"{name}: ${info['price']} | Seats Available: {info['seats']}")
    print("-------------------------------")

def book_ticket(movies):
    movie_name = input("Enter movie name to book: ")
    if movie_name not in movies:
        print("Movie not found.\n")
        return
    try:
        seats = int(input(f"How many seats for '{movie_name}'? "))
        if seats <= 0:
            print("Number of seats must be positive.\n")
            return
        available = movies[movie_name]['seats']
        if seats > available:
            print(f"Only {available} seats available for '{movie_name}'.\n")
            return
        movies[movie_name]['seats'] -= seats
        total = seats * movies[movie_name]['price']
        print(f"Booked {seats} seat(s) for '{movie_name}'. Total: ${total}\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def main():
    movies = {
        "Avengers": {"seats": 10, "price": 1500},
        "Inception": {"seats": 8, "price": 1200},
        "Lion King": {"seats": 5, "price": 1000}
    }
    while True:
        print("Movie Ticket Booking System")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. Exit")
        print()
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            show_movies(movies)
        elif choice == "2":
            show_movies(movies)
            book_ticket(movies)
        elif choice == "3":
            print("Goodbye! Enjoy your movie.")
            break
        else:
            print("Invalid choice. Please select 1-3.\n")

main()