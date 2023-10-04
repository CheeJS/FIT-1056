from week09_user import User
class Admin(User):
    def __init__(self, fName, lName, username, password, role="AD", is_active=True):
        super().__init__(fName, lName, username, password, role=role, is_active=is_active)

