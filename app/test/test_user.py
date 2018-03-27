import unittest
from Project2.user.user import User
from Project2.project2.borrowlist import BorrowList

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_details = ("test2@gmail.com", "Password", "Kushim Eckhart")
        self.user_instance = User(*self.user_details)
        self.borrowlist_details = ("ItemName", "Description:optional")
        self.borrowlist = BorrowList(*self.borrowlist_details, owner=self.user_details[0])

    def test_user_is_created(self):
        self.assertEqual(self.user_instance.name, self.user_details[2])
        self.assertEqual(self.user_instance.password, self.user_details[1])
        self.assertEqual(self.user_instance.email, self.user_details[0])
    def test_user_inherits_from_user(self):
        self.assertEqual(isinstance(self.user_instance, user), True)
    def test_user_representation(self):
        self.assertEqual(str(self.user_instance), "Kushim Eckhart")

if __name__ == '__main__':
    unittest.main()
