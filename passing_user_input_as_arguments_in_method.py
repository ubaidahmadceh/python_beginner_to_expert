class library:
    def __init__(self, book_type, book_name, book_author, book_edition):
        self.book = book_name
        self.type = book_type
        self.author = book_author
        self.edition = book_edition

    def show_book(self):
        print(f"Book name is {self.book} || Book type is {self.type} || Book author is {self.author} || Book edition is {self.edition}")

book = input("Enter book : ")
book_type = input("Enter type : ")
author = input("Enter author : ")
edition = input("Enter edition : ")

object_of_library = library(book_type, book, author, edition)
object_of_library.show_book()
