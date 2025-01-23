class Library:
    def _init__(self):
        self.name = "Tinashe's Library"
        self.address = "36 Lansville Road"
        self.book = ["OOP Project", "Divergent", "Harry Potter"]
        self.borrowings = borrowings

    def borrow_book(self, book_id, user_id, librarian_id):
        self.borrowings.append(self.book(book_id))
        print(self.borrowings)


    def check(self):
        print(self.__price)

class Borrowing:
    def __init__(self, user_id, book, borrow_date, return_date, librarian_id):
        user_id = ""
        book = ""
        borrow_date = ""
        return_date = ""
        librarian_id = ""


class Book:
    def __init__(self, title, author, id_number, category, __price):
        self.title = "OOP Project"
        self.author = "Tinashe Murungweni"
        self.id_number = "34676"
        self.category = "Information & Technology"
        self.__price = 8.99




class Person:
    pass

class User(Person):
    pass

class Librarian(Person):
    pass

    



