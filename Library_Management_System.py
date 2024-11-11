# Library Management System

# Sample book data
books = []

# Function to add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    books.append({'title': title, 'author': author, 'genre': genre, 'available': True})
    print(f"Book '{title}' added.\n")


# Function to delete a book
def delete_book():
    title = input("Enter the title of the book to delete: ")
    for book in books:
        if book['title'] == title:
            books.remove(book)
            print(f"Book '{title}' deleted.\n")
            return
    print(f"Book '{title}' not found.\n")


# Function to borrow a book
def borrow_book():
    title = input("Enter the title of the book to borrow: ")
    for book in books:
        if book['title'] == title and book['available']:
            book['available'] = False
            print(f"You have borrowed '{title}'.\n")
            return
        elif book['title'] == title:
            print(f"Book '{title}' is not available.\n")
            return
    print(f"Book '{title}' not found.\n")


# Function to return a book
def return_book():
    title = input("Enter the title of the book to return: ")
    for book in books:
        if book['title'] == title:
            book['available'] = True
            print(f"You have returned '{title}'.\n")
            return
    print(f"Book '{title}' not found.\n")


# Function to search for books
def search_books():
    query = input("Enter title, author, or genre to search: ")
    results = [book for book in books if
               query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or query.lower() in
               book['genre'].lower()]
    if results:
        for book in results:
            print(
                f"Found: {book['title']} by {book['author']} - Genre: {book['genre']} - {'Available' if book['available'] else 'Not Available'}\n")
    else:
        print("No books found.\n")

# Menu Function
def menu():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            search_books()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()