from borrowlist_item import BorrowListItem

class BorrowList(object):

    def __init__(self, name, details=None, items=None, owner=None):
        self.name = name
        self.details = details
        self.items = []
        self.owner = owner

    def add_item(self, item_details, owner):
        item_name = item_details[0]

        if item_name in self.items:
            raise Exception("You already added {}".format(item_name))
        new_item = BorrowListItem(*item_details, borrowlist=owner)
        self.items.append(new_item)
        return(new_item, "You have borrowed {}.".format(item_name))
    def remove_item(self, borrowlist_item):
        if borrowlist_item not in self.items:
            raise Exception("You do not have {}.".format(borrowlist_item))
        self.items.remove(borrowlist_item)
        return "You have returned {}.".format(borrowlist_item)

    def __repr__(self):
        return self.name
