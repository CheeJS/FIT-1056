from User import User
class Student(User):
    def __init__(self, fName, lName, username, password, role="LR", is_active=True):
        super().__init__(fName, lName, username, password, role=role, is_active=is_active)
        self.all_quizzes = {}
        self.attempted_quizzes = {}