'''
This file constructs of the admin class, containing information of the admin's name, username, password, role and status.
'''

from User import User
class Admin(User):
    
    def __init__(self, fName, lName, username, password, role="AD", is_active=True):
        """
        Create an instance of the Admin class with the specified user information.
        Parameters:
        fName (str): The first name of the admin user
        lName (str): The last name of the admin user
        username (str): The username of the admin user
        password (str): The password of the admin user
        role (str, optional): The role of the admin user (default is "AD")
        is_active (bool, optional): Whether the admin user is active or not (default is True)
        Return: Admin - An instance of the Admin class representing the admin user
        """
        super().__init__(fName, lName, username, password, role=role, is_active=is_active)
