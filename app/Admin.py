

from app.book.book import Book


class LibraryAdmin:
    ''' Perfoming CRUD operations on books '''

    def __init__(self, user):
        ''' Construct the library controller '''
        self.user = user
        self.available_books = []

    def add_book(self, book_details):
        ''' Functionality to create new book '''
        book_name = book_details[0]
        if book_name in self.available_books:
            raise Exception("A book with the name {} already exists")
        # add name of new book to list of available books. the book instance is from an object from a different file
        new_book = Book(*book_details, owner=self.user)
        self.available_books.append(new_book)
        return (new_book, "{} book has been added".format(new_book))

    def update_book_details(self, target_book, new_book_details):
        ''' Functionality to update book details '''
        target_book.name, target_book.details = (new_book_details)
        return "{} has been updated accordingly".format(target_book.name)

    def delete_book(self, book):
        ''' Functionality to delete book '''
        self.available_books.remove(book)
        return "VICTORY you have deleted {}".format(book)
