#this tests the capabilities a user has in the website
import unittest
import app
from app.borrowlist import BorrowList

from app.borrowlist_item import BorrowListItem

class TestBorrowList(unittest.TestCase): 
    def setUp(self):
        self.borrowlist_owner = "Account holder"
        self.new_borrowlist = BorrowList("Sample list", owner=self.borrowlist_owner)
        self.new_item_details = ("ItemName", "Category", "Description:optional")

        #Begin by testing for the successful instatiation of new_borrowlist instance
    def test_borrowlist_is_made(self):
        self.assertEqual(isinstance(self.new_borrowlist, BorrowList), True)

    def test_borrowlist_items_in_list(self):
        self.assertEqual(isinstance(self.new_borrowlist.items, list), True)
    
    def test_borrowlist_has_owner(self):
        self.assertNotEqual(self.new_borrowlist.owner, None)

        #then have tests to check the behaviour of the borrowlist including add, and removing book items to and from the borrowlist

    def test_add_borrowlist_item(self):
        new_item = self.new_borrowlist.add_item(self.new_item_details, self.borrowlist_owner)

        self.assertEqual(new_item[1], "ItemName borrowed")
        self.assertIn(new_item[0], self.new_borrowlist.items)
        self.assertEqual(isinstance(new_item[0], BorrowListItem), True)
    
    def test_remove_borrowlist_item(self):
        new_item = self.new_borrowlist.add_item(self.new_item_details, self.borrowlist_owner)

        remove_item = self.new_borrowlist.remove_item(new_item[0])
        self.assertEqual(remove_item, "You have returned {}".format(self.new_item_details[0]))
        self.assertEqual(new_item in self.new_borrowlist.items, False)

        #testing for the possible edge cases
    def test_adding_similar_borrowlist_items_twice(self):
        self.assertRaises(Exception, self.new_borrowlist.add_item, self.new_item_details)

    def test_deleting_not_in_borrowlist(self):
        self.assertRaises(Exception, self.new_borrowlist.remove_item, self.new_item_details[0] )

if __name__ == '__main__':
    unittest.main()
