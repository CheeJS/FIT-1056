from User import User
from Quiz import Quiz
from Learner import Learner
from tkinter import messagebox,simpledialog
import tkinter as tk
from Lesson import Lesson

class Teacher(User):
    def __init__(self, fName, lName, username, password):
        super().__init__(fName, lName, username, password, "Teacher")



    def register_learner(self, firstname, lastname, username, password,registered_users):
        # Create a new learner and add them to the list of registered users
        learner = Learner(firstname, lastname, username, password)
        registered_users[username] = learner
        return learner
    def authenticate_teacher(username, password,registered_users):

        teacher = registered_users.get(username)
        if teacher and teacher.password == password and teacher.role == "Teacher":
            return teacher
        return None
    def add_quiz(self, quizzes):
        def submit_quiz():
            title = title_entry.get()
            question_text = question_text_widget.get("1.0", tk.END).strip()
            answer_text = answer_text_widget.get("1.0", tk.END).strip()

            if title and question_text and answer_text:
                # Process the question and answer
                choices_and_correct = answer_text.split(",")
            
                if len(choices_and_correct) != 5:
                    messagebox.showerror("Invalid Question", "A question must have exactly 4 choices and a correct choice index.")
                    return

                question = {
                    "text": question_text,
                    "choices": choices_and_correct[:4],
                    "correct_choice_index": int(choices_and_correct[4])
                }

                # Create the quiz with a single question
                quiz = Quiz(len(quizzes) + 1, title, [question])
                quizzes[quiz.quiz_id] = quiz
                quiz.answer = int(choices_and_correct[4])
                messagebox.showinfo("Quiz Added", f"Quiz ID: {quiz.quiz_id}, Title: {quiz.title}")
                quiz_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        quiz_window = tk.Toplevel()
        quiz_window.title("Create Quiz")

        title_label = tk.Label(quiz_window, text="Title:")
        title_label.pack()

        title_entry = tk.Entry(quiz_window)
        title_entry.pack()

        question_label = tk.Label(quiz_window, text="Question:")
        question_label.pack()

        question_text_widget = tk.Text(quiz_window, height=4, width=60)
        question_text_widget.pack()

        answer_label = tk.Label(quiz_window, text="Correct Answer (Format: Comma-separated correct choice index, 0 to 3):")
        answer_label.pack()

        answer_text_widget = tk.Text(quiz_window, height=2, width=60)
        answer_text_widget.pack()

        submit_button = tk.Button(quiz_window, text="Submit", command=submit_quiz)
        submit_button.pack()

    
    def add_lesson(self,lessons):
        def submit_lesson():
            title = title_entry.get()
            content = content_text.get("1.0", tk.END)

            if title and content:
                lesson = Lesson(len(lessons) + 1, title, content)
                lessons[lesson.lesson_id] = lesson
                messagebox.showinfo("Lessons Added", f"Lesson ID: {lesson.lesson_id} Title: {lesson.title}")
                lesson_window.destroy()
            else:
                tk.messagebox.showerror("Error", "Please fill in all fields.")

        lesson_window = tk.Toplevel()
        lesson_window.title("Add Lesson")

        title_label = tk.Label(lesson_window, text="Title:")
        title_label.pack()

        title_entry = tk.Entry(lesson_window)
        title_entry.pack()

        content_label = tk.Label(lesson_window, text="Content:")
        content_label.pack()

        content_text = tk.Text(lesson_window, height=10, width=40)
        content_text.pack()

        submit_button = tk.Button(lesson_window, text="Submit", command=submit_lesson)
        submit_button.pack()
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
    def register_learner(self,registered_users):
        # Create a pop-up window for teacher registration
        register_window = tk.Toplevel()
        register_window.title("Register New Learner")

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
if __name__ == "__main__":
    pass