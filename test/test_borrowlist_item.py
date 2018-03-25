import unittest
from borrowlist_item import BorrowListItem

class TestBorrowListItem(unittest.TestCase):
    def setUp(self):
        self.name, self.category, self.description="borrowlist_item_name"
        "category","description: optional"
    def test_borrowlist_item_is_created(self):
        self.assertTrue(isinstance(self.borrowlist_item, BorrowListItem))
    def test_borrowlist_item_belongs_to_borrowlist(self):
        self.assertNotEqual(self.borrowlist_item.borrowlist_id, None)  
        
if __name__ == '__main__':
    unittest.main()
