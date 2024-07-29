# book.py

# Define the Book class with attributes and methods
class Book:
    def __init__(self, title, author, isbn, publication_date, genre):
        # Initialize a book with title, author, ISBN, publication date, genre, and availability status
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__genre = genre
        self.__availability = True

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def publication_date(self):
        return self.__publication_date

    @property
    def genre(self):
        return self.__genre

    @property
    def availability(self):
        return self.__availability

    @availability.setter
    def availability(self, status):
        self.__availability = status

    def __str__(self):
        # Return a string representation of the book
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}, Available: {self.__availability}"


# Define the FictionBook class inheriting from Book
class FictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, genre, fiction_subgenre):
        # Initialize a fiction book with an additional attribute for fiction subgenre
        super().__init__(title, author, isbn, publication_date, genre)
        self.__fiction_subgenre = fiction_subgenre

    @property
    def fiction_subgenre(self):
        return self.__fiction_subgenre

    def __str__(self):
        # Return a string representation of the fiction book including the subgenre
        return super().__str__() + f", Fiction Subgenre: {self.__fiction_subgenre}"


# Define the NonFictionBook class inheriting from Book
class NonFictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, genre, field_of_study):
        # Initialize a non-fiction book with an additional attribute for field of study
        super().__init__(title, author, isbn, publication_date, genre)
        self.__field_of_study = field_of_study

    @property
    def field_of_study(self):
        return self.__field_of_study

    def __str__(self):
        # Return a string representation of the non-fiction book including the field of study
        return super().__str__() + f", Field of Study: {self.__field_of_study}"


# user.py

# Define the User class with attributes and methods
class User:
    def __init__(self, name, user_id):
        # Initialize a user with name, ID, and an empty list of borrowed books
        self.__name = name
        self.__user_id = user_id
        self.__borrowed_books = []

    @property
    def name(self):
        return self.__name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        # Borrow a book if it's available and add it to the user's borrowed list
        if book.availability:
            self.__borrowed_books.append(book)
            book.availability = False
            return True
        return False

    def return_book(self, book):
        # Return a book if it's in the user's borrowed list and update its availability
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.availability = True
            return True
        return False

    def __str__(self):
        # Return a string representation of the user including borrowed book titles
        borrowed_titles = ', '.join([book.title for book in self.__borrowed_books])
        return f"Name: {self.__name}, User ID: {self.__user_id}, Borrowed Books: {borrowed_titles}"


# author.py

# Define the Author class with attributes
class Author:
    def __init__(self, name, biography):
        # Initialize an author with name and biography
        self.__name = name
        self.__biography = biography

    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

    def __str__(self):
        # Return a string representation of the author
        return f"Name: {self.__name}, Biography: {self.__biography}"


# genre.py

# Define the Genre class with attributes
class Genre:
    def __init__(self, name, description, category):
        # Initialize a genre with name, description, and category
        self.__name = name
        self.__description = description
        self.__category = category

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def category(self):
        return self.__category

    def __str__(self):
        # Return a string representation of the genre
        return f"Name: {self.__name}, Description: {self.__description}, Category: {self.__category}"


# library_management.py

from book import Book, FictionBook, NonFictionBook
from user import User
from author import Author
from genre import Genre

class LibraryManagement:
    def __init__(self):
        # Initialize library management with empty lists for books, users, authors, and genres
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, book):
        # Add a book to the library's book list
        self.books.append(book)

    def borrow_book(self, user_id, isbn):
        # Find user and book by ID and ISBN, then allow the user to borrow the book if available
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book:
            return user.borrow_book(book)
        return False

    def return_book(self, user_id, isbn):
        # Find user and book by ID and ISBN, then allow the user to return the book if borrowed
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book:
            return user.return_book(book)
        return False

    def search_book(self, isbn):
        # Find and return a book by its ISBN
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_books(self):
        # Print all books in the library
        for book in self.books:
            print(book)

    def add_user(self, user):
        # Add a user to the library's user list
        self.users.append(user)

    def display_users(self):
        # Print all users in the library
        for user in self.users:
            print(user)

    def add_author(self, author):
        # Add an author to the library's author list
        self.authors.append(author)

    def display_authors(self):
        # Print all authors in the library
        for author in self.authors:
            print(author)

    def add_genre(self, genre):
        # Add a genre to the library's genre list
        self.genres.append(genre)

    def display_genres(self):
        # Print all genres in the library
        for genre in self.genres:
            print(genre)


# cli.py

from library_management import LibraryManagement
from book import Book, FictionBook, NonFictionBook
from user import User
from author import Author
from genre import Genre

def main():
    library = LibraryManagement()

    while True:
        # Main menu for the library management system
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            # Book operations menu
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")

            book_choice = input("Select an option: ")

            if book_choice == '1':
                # Add a new book
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                publication_date = input("Enter publication date: ")
                genre = input("Enter genre: ")
                library.add_book(Book(title, author, isbn, publication_date, genre))
            elif book_choice == '2':
                # Borrow a book
                user_id = input("Enter user ID: ")
                isbn = input("Enter book ISBN: ")
                if library.borrow_book(user_id, isbn):
                    print("Book borrowed successfully.")
                else:
                    print("Unable to borrow book.")
            elif book_choice == '3':
                # Return a book
                user_id = input("Enter user ID: ")
                isbn = input("Enter book ISBN: ")
                if library.return_book(user_id, isbn):
                    print("Book returned successfully.")
                else:
                    print("Unable to return book.")
            elif book_choice == '4':
                # Search for a book
                isbn = input("Enter book ISBN: ")
                book = library.search_book(isbn)
                if book:
                    print(book)
                else:
                    print("Book not found.")
            elif book_choice == '5':
                # Display all books
                library.display_books()

        elif choice == '2':
            # User operations menu
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")

            user_choice = input("Select an option: ")

            if user_choice == '1':
                # Add a new user
                name = input("Enter name: ")
                user_id = input("Enter user ID: ")
                library.add_user(User(name, user_id))
            elif user_choice == '2':
                # View user details
                user_id = input("Enter user ID: ")
                user = next((u for u in library.users if u.user_id == user_id), None)
                if user:
                    print(user)
                else:
                    print("User not found.")
            elif user_choice == '3':
                # Display all users
                library.display_users()

        elif choice == '3':
            # Author operations menu
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")

            author_choice = input("Select an option: ")

            if author_choice == '1':
                # Add a new author
                name = input("Enter author name: ")
                biography = input("Enter author biography: ")
                library.add_author(Author(name, biography))
            elif author_choice == '2':
                # View author details
                name = input("Enter author name: ")
                author = next((a for a in library.authors if a.name == name), None)
                if author:
                    print(author)
                else:
                    print("Author not found.")
            elif author_choice == '3':
                # Display all authors
                library.display_authors()

        elif choice == '4':
            # Genre operations menu
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")

            genre_choice = input("Select an option: ")

            if genre_choice == '1':
                # Add a new genre
                name = input("Enter genre name: ")
                description = input("Enter genre description: ")
                category = input("Enter genre category: ")
                library.add_genre(Genre(name, description, category))
            elif genre_choice == '2':
                # View genre details
                name = input("Enter genre name: ")
                genre = next((g for g in library.genres if g.name == name), None)
                if genre:
                    print(genre)
                else:
                    print("Genre not found.")
            elif genre_choice == '3':
                # Display all genres
                library.display_genres()

        elif choice == '5':
            # Quit the application
            print("Quitting the application.")
            break

if __name__ == "__main__":
    main()
