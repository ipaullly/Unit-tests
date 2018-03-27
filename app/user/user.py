from app.borrowlist.admin import BorrowListAdmin

class User(BorrowListAdmin):
    def __init__(self, email, password, name):
        BorrowListAdmin.__init__(self, email)
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "{}".format(self.name)
