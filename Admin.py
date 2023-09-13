from User import User

class Admin(User):
    def __init__(self,fName,lName,username,password):
        super().__init__(fName,lName,username,password,"Admin")
        
    def view_students(self, users):
        print("Students:")
        for user in users:
            if user.role == "Learner":
                print(f"- {user.firstname} {user.lastname}")

    def view_teachers(self, users):
        print("Teachers:")
        for user in users:
            if user.role == "Teacher":
                print(f"- {user.firstname} {user.lastname}")

    def manage_user(self):
        print("ma")

if __name__ == "__main__":
    # Create some user objects (students and teachers)
    user1 = User("Alice", "Smith", "alice123", "password123", "Learner")
    user2 = User("Bob", "Johnson", "bob456", "password456", "Learner")
    user3 = User("Teacher", "Smith", "teacher1", "teacherpass", "Teacher")
    user4 = User("Admin", "Admin", "admin1", "adminpass", "Admin")

    # Create an Admin object
    admin = Admin("Admin", "Admin", "admin1", "adminpass")

    # Call the admin's methods
    admin.view_students([user1, user2, user3, user4])
    admin.view_teachers([user1, user2, user3, user4])
    


