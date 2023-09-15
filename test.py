'''
README: 

Still half way development, 

For Learners:
-View grades (Not yet Implemented)
-View Lessons (Done)
-Attempt Quiz (Half way,, buggy)

For Teachers:
- View Learners (Done)
- Register New Learners (Done)
- Add Lessons (Done)
- Add Quizzes (Done)
- View Student grades (Not yet Implemented)

For Admin:
- Register New Learners (Done)
- Register New Teachers (Done)
- View Learners (Done)
- View Teacher (Done)

In main() I created 3 users scroll down and see their username and password to login
In terms of making UI pretty not yet lol
'''

import tkinter as tk
from tkinter import messagebox
from Admin import Admin
from Learner import Learner
from Teacher import Teacher


def login_menu(registered_users,lessons,quizzes):
    root = tk.Tk()
    root.title("Code Venture")
    root.geometry("400x300")  # Set the window size

    window_width = 400
    window_height = 300

    # Calculate the x and y positions to center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window size and position it in the center
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    login_frame = tk.Frame(root)
    login_frame.pack(expand=True, fill="both", padx=20, pady=20)

    username_label = tk.Label(login_frame, text="Username:", font=("Arial", 14))
    username_label.pack(pady=10)

    username_entry = tk.Entry(login_frame, font=("Arial", 14), width=20)
    username_entry.pack(pady=5)

    password_label = tk.Label(login_frame, text="Password:", font=("Arial", 14))
    password_label.pack(pady=10)

    password_entry = tk.Entry(login_frame, show="*", font=("Arial", 14), width=20)
    password_entry.pack(pady=5)

    login_button = tk.Button(login_frame, text="Login", command=lambda: login(username_entry.get(), password_entry.get(), registered_users,root,lessons,quizzes), font=("Arial", 16))
    login_button.pack(pady=20)

    root.mainloop()
def login(username, password, registered_users,root,lessons,quizzes):
    authenticated_admin = Admin.authenticate_admin(username, password, registered_users)
    authenticated_teacher = Teacher.authenticate_teacher(username, password, registered_users)
    authenticated_learner = Learner.authenticate_learner(username, password, registered_users)
    if authenticated_admin:
        root.destroy()
        admin_main(authenticated_admin, registered_users,lessons,quizzes)
    elif authenticated_teacher:
        root.destroy()
        teacher_main(authenticated_teacher, registered_users,lessons,quizzes)
    elif authenticated_learner:
        root.destroy()
        learner_main(authenticated_learner, registered_users,lessons,quizzes)
    else:
        messagebox.showerror("Login Failed", "Authentication failed. Please check your credentials.")

def logout(admin_window,registered_users,lessons,quizzes):
    admin_window.destroy()  # Destroy the admin window
    login_menu(registered_users,lessons,quizzes)



def teacher_main(authenticated_teacher:Teacher, registered_users,lessons,quizzes):
    teacher_window = tk.Tk()
    teacher_window.title("Teacher Dashboard")
    teacher_window.geometry("800x600")  # Set the size of the admin window

    # Create and place teacher interface widgets
    label = tk.Label(teacher_window, text=f"Welcome, {authenticated_teacher.username}!", font=("Arial", 16))
    label.pack(pady=20)

    # Buttons for teacher actions
    view_learner_button = tk.Button(teacher_window, text="View Learners", command=lambda: authenticated_teacher.view_students(registered_users), font=("Arial", 14))
    view_learner_button.pack()

    ##view_learner_grade_button = tk.Button(teacher_window, text="View Learners' grade", command=lambda: authenticated_teacher.view_grade(registered_users), font=("Arial", 14))
    ##view_learner_grade_button.pack()

    register_learner_button = tk.Button(teacher_window, text="Register New Learner", command=lambda:authenticated_teacher.register_learner(registered_users), font=("Arial", 14))
    register_learner_button.pack()

    add_lessons_button = tk.Button(teacher_window, text="Add Lessons", command=lambda:authenticated_teacher.add_lesson(lessons), font=("Arial", 14))
    add_lessons_button.pack()

    add_quizzes_button = tk.Button(teacher_window, text="Add Quizzes", command=lambda:authenticated_teacher.add_quiz(quizzes), font=("Arial", 14))
    add_quizzes_button.pack()

    logout_button = tk.Button(teacher_window, text="Log Out", command=lambda:logout(teacher_window,registered_users,lessons,quizzes), font=("Arial", 14))
    logout_button.pack(pady=20)

    teacher_window.mainloop()

def learner_main(authenticated_learner:Learner, registered_users,lessons,quizzes):
    learner_window = tk.Tk()
    learner_window.title("Learner Dashboard")
    learner_window.geometry("800x600")  # Set the size of the admin window

    # Create and place learner interface widgets
    label = tk.Label(learner_window, text=f"Welcome, {authenticated_learner.username}!", font=("Arial", 16))
    label.pack(pady=20)

    # Buttons for learner actions

    view_lessons_button = tk.Button(learner_window, text="View Lessons", command=lambda:authenticated_learner.view_lessons(lessons), font=("Arial", 14))
    view_lessons_button.pack()

    attempt_quiz_button = tk.Button(learner_window, text="Attempt quizzes (Half Way)", command=lambda:authenticated_learner.attempt_quiz(quizzes), font=("Arial", 14))
    attempt_quiz_button.pack()

    view_grade__button = tk.Button(learner_window, text="View your grades (Not Yet)", command=lambda:authenticated_learner.register_learner(registered_users), font=("Arial", 14))
    view_grade__button.pack()

    logout_button = tk.Button(learner_window, text="Log Out", command=lambda:logout(learner_window,registered_users,lessons,quizzes), font=("Arial", 14))
    logout_button.pack(pady=20)

    learner_window.mainloop()

def admin_main(authenticated_admin :Admin,registered_users,lessons,quizzes):
    admin_window = tk.Tk()
    admin_window.title("Admin Dashboard")
    admin_window.geometry("800x600")  # Set the size of the admin window

    # Create and place admin interface widgets
    label = tk.Label(admin_window, text=f"Welcome, {authenticated_admin.username}!", font=("Arial", 16))
    label.pack(pady=20)

    # Buttons for admin actions
    view_teachers_button = tk.Button(admin_window, text="View Teachers", command=lambda: authenticated_admin.view_teachers(registered_users), font=("Arial", 14))
    view_teachers_button.pack()

    view_learners_button = tk.Button(admin_window, text="View Learners", command=lambda:authenticated_admin.view_students(registered_users), font=("Arial", 14))
    view_learners_button.pack()

    register_teacher_button = tk.Button(admin_window, text="Register New Teacher", command=lambda:authenticated_admin.register_teacher(registered_users), font=("Arial", 14))
    register_teacher_button.pack()

    register_learner_button = tk.Button(admin_window, text="Register New Learner", command=lambda:authenticated_admin.register_learner(registered_users), font=("Arial", 14))
    register_learner_button.pack()

    logout_button = tk.Button(admin_window, text="Log Out", command=lambda:logout(admin_window,registered_users,lessons,quizzes), font=("Arial", 14))
    logout_button.pack(pady=20)

    admin_window.mainloop()
    


def main():
    registered_users = {}
    lessons = {}
    quizzes = {}
    admin1 = Admin("Admin1", "Admin1", "admin", "adminpw")
    admin2 = Admin("Admin2", "Admin2", "admin2", "admin2pw")
    user = Teacher("123", "123", "123", "123")
    user2 = Learner("1","1","1","1")
    registered_users[admin1.username] = admin1
    registered_users[admin2.username] = admin2
    registered_users[user.username] = user
    registered_users[user2.username] = user2
    login_menu(registered_users,lessons,quizzes)

    

if __name__ == "__main__":
    main()
    ## Questions 1 "What is the capital of France?" , "Paris,New York,London,Berlin,0"
    ## Question 2 "What is the capital of Germany?" , "Berlin,Paris,London,New York,2"

