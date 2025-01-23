class Library:
    name = "Tinashe's Library"
    address = "36 Lansville Road"
    books = ["OOP Project", "Divergent", "Harry Potter"]
    borrowings = []

    def borrow_book(self, book_id, user_id, librarian_id):
        self.borrowings.append(self.books[book_id])
        print(f" {user_id} has borrowed {self.borrowings}")

    def return_book(self, book_id, user_id, librarian_id):
        self.borrowings.pop(self.borrowings[book_id])
        print(f" {user_id} returned {self.borrowings}")