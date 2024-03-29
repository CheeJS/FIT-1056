class User:
    """
    Class definition for the User class
    """

    def __init__(self,fName,lName, username, password, role=None, is_active=True):
        self.__firstName = fName
        self.__lastName = lName
        self.__username = username
        self.__password = password
        self.__role = role
        self.__is_active = is_active

    def get_firstName(self):
        return self.__firstName
    
    def get_lastName(self):
        return self.__lastName

    def get_username(self):
        """
        Getter for the username attribute.
        :return: str
        """
        return self.__username

    def get_password(self):
        """
        Getter for the password attribute.
        :return: str
        """
        return self.__password

    def get_role(self):
        """
        Getter for the role attribute.
        :return: str
        """
        return self.__role

    def get_is_active(self):
        """
        Getter for the is_active attribute.
        :return: bool
        """
        return self.__is_active
    


if __name__ == "__main__":
    pass
