

from Project2.project2.borrowlist import BorrowList


class BorrowListAdmin(object):
    ''' This class has subclasses that provide functionalities to the site administrator '''

    def __init__(self, user):
        ''' Initialise an instance of libraryadmin '''
        self.user = user
        self.available_borrowlists = []
    def update_borrowlist_details(self, target_borrowlist, new_borrowlist_details):
        ''' this method allows the admin to update book details '''
        target_borrowlist.name, target_borrowlist.details = (new_borrowlist_details)
        return "{} has been updated accordingly".format(target_borrowlist.name)

    def add_borrowlist(self, borrowlist_details):
        ''' this enables admin to create new list item ie book '''
        borrowlist_name = borrowlist_details[0]
        if borrowlist_name in self.available_borrowlists:
            raise Exception("A book with the name {} already exists")
        # add name of new book to list of available books. the book instance is from an object from a different file
        new_borrowlist = BorrowList(borrowlist_details, owner=self.user)
        self.available_borrowlists.append(new_borrowlist)
        return (new_borrowlist, "{} book has been added".format(new_borrowlist))

    def delete_borrowlist(self, borrowlist):
        ''' enables site administrator to delete book '''
        self.available_borrowlists.remove(borrowlist)
        return "VICTORY you have deleted {}".format(borrowlist)
