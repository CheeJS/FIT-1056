from User import User
class Teacher(User):
    """
    Class definition for the Teacher class
    """
    def __init__(self, fName, lName, username, password, role="TA", is_active=True):
        """
        Create an instance of the Teacher class with the specified user information.
        Parameters:
        fName (str): The first name of the Teacher user
        lName (str): The last name of the Teacher user
        username (str): The username of the Teacher user
        password (str): The password of the Teacher user
        role (str, optional): The role of the Teacher user (default is "TA")
        is_active (bool, optional): Whether the admin user is active or not (default is True)
        Return: Teacher - An instance of the Teacher class representing the Teacher user
        """
        super().__init__(fName, lName, username, password, role=role, is_active=is_active)