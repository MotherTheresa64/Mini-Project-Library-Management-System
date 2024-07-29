class Book:
    def __init__(self, title, author, isbn, publication_date, genre):
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
        if isinstance(status, bool):
            self.__availability = status
        else:
            raise ValueError("Availability must be a boolean value")

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}, Available: {self.__availability}"

class FictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, genre, fiction_subgenre):
        super().__init__(title, author, isbn, publication_date, genre)
        self.__fiction_subgenre = fiction_subgenre

    @property
    def fiction_subgenre(self):
        return self.__fiction_subgenre

    def __str__(self):
        return super().__str__() + f", Fiction Subgenre: {self.__fiction_subgenre}"

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, genre, field_of_study):
        super().__init__(title, author, isbn, publication_date, genre)
        self.__field_of_study = field_of_study

    @property
    def field_of_study(self):
        return self.__field_of_study

    def __str__(self):
        return super().__str__() + f", Field of Study: {self.__field_of_study}"
