class Library:
    name = "Tinashe's Library"
    address = "36 Lansville Road"
    books = ["OOP Project", "Divergent", "Harry Potter"]
    borrowings = []

    def borrow_book(self, book_id, user_id, librarian_id):
        self.borrowings.append(self.books[book_id])
        print(self.borrowings)

    """def return_book(self, book_id, user_id, librarian_id):
        self.books."""