class User:
    def __init__(self, name, user_id):
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
        if book.availability:
            self.__borrowed_books.append(book)
            book.availability = False
            return True
        return False

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.availability = True
            return True
        return False

    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.__borrowed_books])
        return f"Name: {self.__name}, User ID: {self.__user_id}, Borrowed Books: {borrowed_titles}"
