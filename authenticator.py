# Local application imports
from User import User
from Admin import Admin
from Student import Student
from Teacher import Teacher

class Authenticator:

    def __init__(self, file_path="./data/user_data.txt"):
        self.file_path = file_path
        self.users = []
        self.load_users()

    def load_users(self):
        """
        Load list of users from the ./data/users.txt file
        :return: bool (True if successful, False otherwise)
        """
        try:
            with open(self.file_path, "r", encoding="utf8") as users_f:
                users_lines = users_f.readlines()
                for line in users_lines:
                    (fName,
                     lName,
                        username,
                     password,
                     role,
                     is_active) = line.strip().split(",")
                    if role == "AD":
                        user_obj = Admin(fName=fName,lName=lName,username=username,password=password,role=role,is_active=bool(is_active))
                    elif role == "TA":
                        user_obj = Teacher(fName=fName,lName=lName,username=username,password=password,role=role,is_active=bool(is_active))
                    elif role == "LR":
                        user_obj = Student(fName=fName,lName=lName,username=username,password=password,role=role,is_active=bool(is_active))
                    self.users.append(user_obj)
            return True
        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist!")
            return False

    def authenticate(self, input_username, input_password):
        """
        Logic for authenticating a login procedure
        :param input_username: str - username entered by the user
        :param input_password: str - password entered by the user
        :return: bool
        """
        for user_obj in self.users:
            if user_obj.get_username() == input_username:
                # If username is found
                if (user_obj.get_password() == input_password
                        and user_obj.get_is_active()):
                    # Passwords match and account is active
                    return True
                else:
                    # Authentication fails or account is no longer active
                    return False
        # Account does not exist
        return False
    def authenticate_get_role(self, input_username, input_password):
        for user_obj in self.users:
            if user_obj.get_username() == input_username:
                # If username is found
                if (user_obj.get_password() == input_password
                        and user_obj.get_is_active()):
                    # Passwords match and account is active
                    return user_obj.get_role()
                else:
                    # Authentication fails or account is no longer active
                    return None
        # Account does not exist
        return None

if __name__ == "__main__":
    pass
