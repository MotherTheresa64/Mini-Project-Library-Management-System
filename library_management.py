from book import Book, FictionBook, NonFictionBook
from user import User
from author import Author
from genre import Genre

class LibraryManagement:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, user_id, isbn):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book:
            return user.borrow_book(book)
        return False

    def return_book(self, user_id, isbn):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if user and book:
            return user.return_book(book)
        return False

    def search_book(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_books(self):
        for book in self.books:
            print(book)

    def add_user(self, user):
        self.users.append(user)

    def display_users(self):
        for user in self.users:
            print(user)

    def add_author(self, author):
        self.authors.append(author)

    def display_authors(self):
        for author in self.authors:
            print(author)

    def add_genre(self, genre):
        self.genres.append(genre)

    def display_genres(self):
        for genre in self.genres:
            print(genre)
