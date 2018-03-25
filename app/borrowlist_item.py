# this object describes the borrowlist item(book) and all their attributes
class BorrowListItem:

    def __init__(self, name, category, description=None, borrowlist=None):
        self.name = name
        self.category = category
        self.description = description
        self.borrowlist_id = borrowlist

    def __repr__(self):
        return self.name
