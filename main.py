from Admin import Admin
from Learner import Learner
from Quiz import Quiz
from Lesson import Lesson
from Teacher import Teacher
import tkinter as tk
from tkinter import messagebox

def test_application():
    # Create users
    learner1 = Learner("Alice", "Smith", "alice123", "password123")
    learner2 = Learner("Bob", "Johnson", "bob456", "password456")

    teacher1 = Teacher("Jake", "Blake", "jake789", "password789")

    admin1 = Admin("Admin", "Admin", "admin1", "adminpass")


    # Create lessons and quizzes
    lesson1 = Lesson(1, "Python Basics", "This is a lesson about Python basics.")
    lesson2 = Lesson(2, "JavaScript Fundamentals", "This is a lesson about JavaScript fundamentals.")
    all_quizzes = [
        Quiz(101, "Python Basics Quiz", ["Question 1", "Question 2"]),
        Quiz(102, "JavaScript Fundamentals Quiz", ["Question 1", "Question 2"]),
        Quiz(103, "HTML Basics Quiz", ["Question 1", "Question 2"])
    ]

    print()
    
    # Users view lessons
    learner1.view_lesson(lesson1)
    learner2.view_lesson(lesson2 )
    print()

    # Users attempt quizzes
    learner1.attempt_quiz(all_quizzes[0], 90)
    learner1.attempt_quiz(all_quizzes[1], 88)
    learner1.view_all_grades()
    print()
    
    #Teacher view student progress
    teacher1.view_student_progress([learner1,learner2], all_quizzes)
    print()
    

    print()
    
    # Print user types
    print(f"{learner1.firstname}'s user type: {learner1.role}")
    print(f"{learner2.firstname}'s user type: {learner2.role}")
    print(f"{teacher1.firstname}'s user type: {teacher1.role}")
    print(f"{admin1.firstname}'s user type: {admin1.role}")
    print()



def learner_menu():
    print("Options:")
    print("\t1. Attempt lessons")
    print("\t1. Attempt quiz")
    print("\t2. View your grade in the system")
    print("\t3. Log out")

# Can register new learner
def teacher_menu():
    print("Options:")
    print("\t1. View names of learners in the system")
    print("\t2. View all of learners grades in the system")
    print("\t3. Register new Learner")
    print("\t4. Log out")

# Can register new student/teacher
def admin_menu():
    print("Options:")
    print("\t1. View names of teachers in the system")
    print("\t2. View names of learners in the system")
    print("\t3. Register new Learner")
    print("\t4. Register new Teacher")
    print("\t5. Log out")

def learner_main(authenticated_learner: Learner, registered_users):
    print()
    print("Successfully logged in as Learner.")
    while True:
        learner_menu()
        print()
        user_input = input("Please enter a menu option: ")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            print("Logging out...")
            break
        else:
            print("You have not entered a valid menu option!", "Please try again.")

def login_menu():
    """
    Prints the menu options for login or shutdown.
    """
    print("Options:")
    print("\t1. Login")
    print("\t2. Shut down")


def teacher_main(authenticated_teacher: Teacher,registered_users):
    print()
    print("Successfully logged in as Teacher.")
    while True:
        teacher_menu()
        print()
        user_input = input("Please enter a menu option: ")
        if user_input == "1":
            pass
        elif user_input == "2":
            authenticated_teacher.view_student_progress()
        elif user_input == "3":
            firstname = input("Enter learner's first name: ")
            lastname = input("Enter learner's last name: ")
            username = input("Enter learner's username: ")
            password = input("Enter learner's password: ")
            learner = authenticated_teacher.register_learner(firstname, lastname, username, password,registered_users)
            print(f"Learner {learner.firstname} {learner.lastname} registered successfully!")
        elif user_input == "4":
            # Log out
            print("Logging out...")
            break
        else:
            print("You have not entered a valid menu option!", "Please try again.")

def admin_main(authenticated_admin :Admin,registered_users):
    
    print()
    print("Successfully logged in as admin.")
    while True:
        admin_menu()
        print()
        user_input = input("Please enter a menu option: ")
        if user_input == "1":
            authenticated_admin.view_teachers(registered_users)
        elif user_input == "2":
            authenticated_admin.view_students(registered_users)
        elif user_input == "3":
            firstname = input("Enter learner's first name: ")
            lastname = input("Enter learner's last name: ")
            username = input("Enter learner's username: ")
            password = input("Enter learner's password: ")
            learner = authenticated_admin.register_learner(firstname, lastname, username, password,registered_users)
            print(f"Learner {learner.firstname} {learner.lastname} registered successfully!")
        elif user_input == "4":
            firstname = input("Enter teacher's first name: ")
            lastname = input("Enter teacher's last name: ")
            username = input("Enter teacher's username: ")
            password = input("Enter teacher's password: ")
            teacher = authenticated_admin.register_teacher(firstname, lastname, username, password,registered_users)
            print(f"Teacher {teacher.firstname} {teacher.lastname} registered successfully!")
        elif user_input == "5":
            # Log out
            print("Logging out...")
            break
        else:
            print("You have not entered a valid menu option!","Please try again.")

def main():
    registered_users = {}
    admin1 = Admin("Admin1", "Admin1", "admin", "adminpw")
    admin2 = Admin("Admin2", "Admin2", "admin2", "admin2pw")
    registered_users[admin1.username] = admin1
    registered_users[admin2.username] = admin2
    print("Welcome to CodeVenture!")
    while True:
        login_menu()
        login_input = input("Please enter a menu option: ")
        if login_input == "1":
            print()
            login_username = input("Please enter your username: ")
            login_password = input("Please enter your password: ")
            authenticated_admin = Admin.authenticate_admin(login_username, login_password,registered_users)
            authenticated_teacher = Teacher.authenticate_teacher(login_username, login_password,registered_users)
            authenticated_Learner = Learner.authenticate_learner(login_username, login_password,registered_users)
            if authenticated_admin:
                admin_main(authenticated_admin,registered_users)
                del authenticated_admin
            elif authenticated_teacher:
                teacher_main(authenticated_teacher,registered_users)
            elif authenticated_Learner:
                learner_main(authenticated_Learner,registered_users)


            

if __name__ == "__main__":

    main()