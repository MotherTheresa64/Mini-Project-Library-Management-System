from library_management import LibraryManagement
from book import Book, FictionBook, NonFictionBook
from user import User
from author import Author
from genre import Genre

def main():
    library = LibraryManagement()

    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")

            book_choice = input("Select an option: ")

            if book_choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                publication_date = input("Enter publication date: ")
                genre = input("Enter genre: ")
                library.add_book(Book(title, author, isbn, publication_date, genre))
            elif book_choice == '2':
                user_id = input("Enter user ID: ")
                isbn = input("Enter book ISBN: ")
                if library.borrow_book(user_id, isbn):
                    print("Book borrowed successfully.")
                else:
                    print("Unable to borrow book.")
            elif book_choice == '3':
                user_id = input("Enter user ID: ")
                isbn = input("Enter book ISBN: ")
                if library.return_book(user_id, isbn):
                    print("Book returned successfully.")
                else:
                    print("Unable to return book.")
            elif book_choice == '4':
                isbn = input("Enter book ISBN: ")
                book = library.search_book(isbn)
                if book:
                    print(book)
                else:
                    print("Book not found.")
            elif book_choice == '5':
                library.display_books()

        elif choice == '2':
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")

            user_choice = input("Select an option: ")

            if user_choice == '1':
                name = input("Enter name: ")
                user_id = input("Enter user ID: ")
                library.add_user(User(name, user_id))
            elif user_choice == '2':
                user_id = input("Enter user ID: ")
                user = next((u for u in library.users if u.user_id == user_id), None)
                if user:
                    print(user)
                else:
                    print("User not found.")
            elif user_choice == '3':
                library.display_users()

        elif choice == '3':
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")

            author_choice = input("Select an option: ")

            if author_choice == '1':
                name = input("Enter author name: ")
                biography = input("Enter author biography: ")
                library.add_author(Author(name, biography))
            elif author_choice == '2':
                name = input("Enter author name: ")
                author = next((a for a in library.authors if a.name == name), None)
                if author:
                    print(author)
                else:
                    print("Author not found.")
            elif author_choice == '3':
                library.display_authors()

        elif choice == '4':
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")

            genre_choice = input("Select an option: ")

            if genre_choice == '1':
                name = input("Enter genre name: ")
                description = input("Enter genre description: ")
                category = input("Enter genre category: ")
                library.add_genre(Genre(name, description, category))
            elif genre_choice == '2':
                name = input("Enter genre name: ")
                genre = next((g for g in library.genres if g.name == name), None)
                if genre:
                    print(genre)
                else:
                    print("Genre not found.")
            elif genre_choice == '3':
                library.display_genres()

        elif choice == '5':
            print("Quitting the application.")
            break

if __name__ == "__main__":
    main()
