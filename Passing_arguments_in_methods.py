class library:
    def __init__(self, book_type, book_name, book_author, book_edition):
        self.book = book_name
        self.type = book_type
        self.author = book_author
        self.edition = book_edition

    def show_book(self):
        print(f"Book name is {self.book} || Book type is {self.type} || Book author is {self.author} || Book edition is {self.edition}")

object_of_library = library("Comic", "Koi bhi name", "Koi bhi Author", "2002")
object_of_library.show_book()
