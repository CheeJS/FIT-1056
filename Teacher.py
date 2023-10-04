from User import User
class Teacher(User):
    def __init__(self, fName, lName, username, password, role="TA", is_active=True):
        super().__init__(fName, lName, username, password, role=role, is_active=is_active)