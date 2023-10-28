from User import User
class Student(User):
    """
    Class definition for the Student class
    """
    def __init__(self, fName, lName, username, password, role="LR", is_active=True):
        """
        Create an instance of the Student class with the specified user information.
        Parameters:
        fName (str): The first name of the Student user
        lName (str): The last name of the Student user
        username (str): The username of the Student user
        password (str): The password of the Student user
        role (str, optional): The role of the Student user (default is "LR")
        is_active (bool, optional): Whether the admin user is active or not (default is True)
        Return: Student - An instance of the Student class representing the Student user
        """
        super().__init__(fName, lName, username, password, role=role, is_active=is_active)
        self.all_quizzes_score = {}
        self.attempted_quizzes = {}

    def get_attempted_quizzes(self):
        """
        return student attemped quiz
        """
        return self.attempted_quizzes
    
    def all_quizzes_score(self):
        """
        return student quiz score
        """
        return self.all_quizzes_score