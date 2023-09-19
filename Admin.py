from User import User
import tkinter as tk
from Learner import Learner
from Teacher import Teacher
from tkinter import messagebox,simpledialog

class Admin(User):
    registered_users = {}
    def __init__(self,fName,lName,username,password):
        super().__init__(fName,lName,username,password,"Admin")

    def view_students(self,registered_users):
        students_list = []
        for username, user in registered_users.items():
            if user.role == "Learner":
                students_list.append(f"Name: {user.firstname} {user.lastname}, Username: {user.username}")

        if not students_list:
            messagebox.showinfo("No Learner Found", "There are no Learner registered.")
            return  # Exit the function if no Learner are found

        learner_info = "\n".join(students_list)

        # Create a new window to display the list of Learner
        learner_window = tk.Tk()
        learner_window.title("List of Learner")

        # Create a label to display the list
        label = tk.Label(learner_window, text="List of Learner", font=("Arial", 16))
        label.pack(pady=10)

        text_widget = tk.Text(learner_window, font=("Arial", 12), height=10, width=40)
        text_widget.insert(tk.END, learner_info)
        text_widget.pack(pady=10)

        learner_window.mainloop()

    def view_teachers(self,registered_users):
   

        teachers_list = []
        for username, user in registered_users.items():
            if user.role == "Teacher":
                teachers_list.append(f"Name: {user.firstname} {user.lastname}, Username: {user.username}")

        if not teachers_list:
            messagebox.showinfo("No Teachers Found", "There are no teachers registered.")
            return  # Exit the function if no teachers are found

        teachers_info = "\n".join(teachers_list)

        # Create a new window to display the list of teachers
        teachers_window = tk.Tk()
        teachers_window.title("List of Teachers")

        # Create a label to display the list
        label = tk.Label(teachers_window, text="List of Teachers", font=("Arial", 16))
        label.pack(pady=10)

        text_widget = tk.Text(teachers_window, font=("Arial", 12), height=10, width=40)
        text_widget.insert(tk.END, teachers_info)
        text_widget.pack(pady=10)

        teachers_window.mainloop()
    def register_learner(self,registered_users):
        # Create a pop-up window for teacher registration
        register_window = tk.Toplevel()
        register_window.title("Register New Learner")
        register_window.geometry("800x600")
        # Create labels and entry fields
        first_name_label = tk.Label(register_window, text="First Name:")
        last_name_label = tk.Label(register_window, text="Last Name:")
        username_label = tk.Label(register_window, text="Username:")
        password_label = tk.Label(register_window, text="Password:")

        first_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        last_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        username_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        first_name_entry = tk.Entry(register_window)
        last_name_entry = tk.Entry(register_window)
        username_entry = tk.Entry(register_window)
        password_entry = tk.Entry(register_window, show="*")

        first_name_entry.grid(row=0, column=1, padx=5, pady=5)
        last_name_entry.grid(row=1, column=1, padx=5, pady=5)
        username_entry.grid(row=2, column=1, padx=5, pady=5)
        password_entry.grid(row=3, column=1, padx=5, pady=5)

        def submit():
            # Get the values from the entry fields
            learner_firstname = first_name_entry.get()
            learner_lastname = last_name_entry.get()
            learner_username = username_entry.get()
            learner_password = password_entry.get()

            if learner_firstname and learner_lastname and learner_username and learner_password:
                # Check if the username is already taken
                if learner_username in registered_users:
                    messagebox.showerror("Registration Failed", "Username is already taken. Please choose a different username.")
                else:
                    learner = Learner(learner_firstname, learner_lastname, learner_username, learner_password)
                    registered_users[learner_username] = learner
                    messagebox.showinfo("Registration Complete", f"Teacher {learner.firstname} {learner.lastname} registered successfully!")
                    register_window.destroy()
            else:
                messagebox.showerror("Registration Failed", "Please fill in all fields.")

        submit_button = tk.Button(register_window, text="Submit", command=submit)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        register_window.mainloop()
    def register_teacher(self, registered_users):
        # Create a pop-up window for teacher registration
        register_window = tk.Toplevel()
        register_window.title("Register New Teacher")
        register_window.geometry("800x600")
        # Create labels and entry fields
        first_name_label = tk.Label(register_window, text="First Name:", font=("Arial", 14))
        last_name_label = tk.Label(register_window, text="Last Name:", font=("Arial", 14))
        username_label = tk.Label(register_window, text="Username:", font=("Arial", 14))
        password_label = tk.Label(register_window, text="Password:", font=("Arial", 14))

        first_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        last_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        username_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        first_name_entry = tk.Entry(register_window)
        last_name_entry = tk.Entry(register_window)
        username_entry = tk.Entry(register_window)
        password_entry = tk.Entry(register_window, show="*")

        first_name_entry.grid(row=0, column=1, padx=5, pady=5)
        last_name_entry.grid(row=1, column=1, padx=5, pady=5)
        username_entry.grid(row=2, column=1, padx=5, pady=5)
        password_entry.grid(row=3, column=1, padx=5, pady=5)

        def submit():
            # Get the values from the entry fields
            teacher_firstname = first_name_entry.get()
            teacher_lastname = last_name_entry.get()
            teacher_username = username_entry.get()
            teacher_password = password_entry.get()

            if teacher_firstname and teacher_lastname and teacher_username and teacher_password:
                # Check if the username is already taken
                if teacher_username in registered_users:
                    messagebox.showerror("Registration Failed", "Username is already taken. Please choose a different username.")
                else:
                    teacher = Teacher(teacher_firstname, teacher_lastname, teacher_username, teacher_password)
                    registered_users[teacher_username] = teacher
                    messagebox.showinfo("Registration Complete", f"Teacher {teacher.firstname} {teacher.lastname} registered successfully!")
                    register_window.destroy()
            else:
                messagebox.showerror("Registration Failed", "Please fill in all fields.")

        submit_button = tk.Button(register_window, text="Submit", command=submit)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        register_window.mainloop()


    @classmethod
    def get_user_by_username(cls, username):
        return cls.registered_users.get(username)

    
    def authenticate_admin(username, password,registered_users):
        admin = registered_users.get(username)
        if admin and admin.password == password and admin.role == "Admin":
            return admin
        return None
    
if __name__ == "__main__":
    pass
    # Create some user objects (students and teachers)
    #user1 = User("Alice", "Smith", "alice123", "password123", "Learner")
    #user2 = User("Bob", "Johnson", "bob456", "password456", "Learner")
    #user3 = User("Teacher", "Smith", "teacher1", "teacherpass", "Teacher")
    #user4 = User("Admin", "Admin", "admin1", "adminpass", "Admin")

    # Create an Admin object
    #admin = Admin("Admin", "Admin", "admin1", "adminpass")

    # Call the admin's methods
    #admin.view_students([user1, user2, user3, user4])
    #admin.view_teachers([user1, user2, user3, user4])
    


