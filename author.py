class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

    def __str__(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
