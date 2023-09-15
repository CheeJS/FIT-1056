from User import User
from Quiz import Quiz
from Lesson import Lesson
from tkinter import messagebox,simpledialog
import tkinter as tk

class Learner(User):
    def __init__(self,fName,lName,username,password):
        super().__init__(fName,lName,username,password,"Learner")


    def attempt_quiz(self, quizzes):
        def submit_quiz():
            quiz_id = quiz_var.get()
            self.quiz_attempts = {}

            if quiz_id in self.quiz_attempts:
                messagebox.showinfo("Quiz Attempted", f"You have already attempted Quiz {quiz_id}.")
                return

            if int(quiz_id) not in quizzes:
                messagebox.showerror("Invalid Quiz", "Invalid quiz selected.")
                return

            quiz = quizzes[int(quiz_id)]
            questions = quiz.questions

            correct_choices = quiz.answer
            print(correct_choices)


            selected_choices = []  # A list of lists to store selected choices for each question
            for i in range(len(questions)):
                selected_choices_question = []
                for j in range(len(questions[i]['choices'])):
                    selected_choices_question.append(choice_vars[i][j].get())
                selected_choices.append(selected_choices_question)

   
            #for item in selected_choices:
            #    print(item)
            #score = sum(1 for i in range(len(selected_choices)) if selected_choices[i] == correct_choices)

            messagebox.showinfo("Quiz Result", f"Your score for Quiz is -.")

            #self.quiz_attempts[quiz_id] = score

        quiz_attempt_window = tk.Toplevel()
        quiz_attempt_window.title("Attempt Quiz")

        quiz_label = tk.Label(quiz_attempt_window, text="Select a Quiz:")
        quiz_label.pack()

        quiz_var = tk.StringVar()
        quiz_var.set("Select a Quiz")

        quiz_dropdown = tk.OptionMenu(quiz_attempt_window, quiz_var, *quizzes.keys())
        quiz_dropdown.pack()

        questions_frame = tk.Frame(quiz_attempt_window)
        questions_frame.pack()

        choice_vars = []

        def load_questions(name, index, mode):
            for widget in questions_frame.winfo_children():
                widget.destroy()
            choice_vars.clear()

            quiz_id = quiz_var.get()
            if quiz_id != "Select a Quiz":
                quiz = quizzes[int(quiz_id)]
                questions = quiz.questions

                for i, question in enumerate(questions):
                    question_label = tk.Label(questions_frame, text=f"Q{i + 1}: {question['text']}")
                    question_label.grid(row=i, column=0, sticky="w")

                    choice_vars_question = []
                    for j, choice in enumerate(question['choices']):
                        choice_var = tk.IntVar()
                        choice_checkbox = tk.Checkbutton(questions_frame, text=choice, variable=choice_var)
                        choice_checkbox.grid(row=i, column=j + 1)
                        choice_vars_question.append(choice_var)
                    choice_vars.append(choice_vars_question)

        quiz_var.trace_add("write", load_questions)

        submit_button = tk.Button(quiz_attempt_window, text="Submit", command=submit_quiz)
        submit_button.pack()


    
    def authenticate_learner(username, password,registered_users):
        Learner = registered_users.get(username)
        if Learner and Learner.password == password and Learner.role == "Learner":
            return Learner
        return None
    def view_lessons(self, lessons):
        if not lessons:
            messagebox.showinfo("No Lessons", "There are no lessons available.")
            return

        def show_lesson_content():
            selected_lesson_title = lesson_var.get()
            if selected_lesson_title:
                selected_lesson = next((lesson for lesson in lessons.values() if lesson.title == selected_lesson_title), None)
                if selected_lesson:
                    lesson_content = selected_lesson.content
                    lesson_content_text.config(state=tk.NORMAL)
                    lesson_content_text.delete("1.0", tk.END)
                    lesson_content_text.insert(tk.END, lesson_content)
                    lesson_content_text.config(state=tk.DISABLED)

        lesson_window = tk.Toplevel()
        lesson_window.title("Lessons")

        label = tk.Label(lesson_window, text="Choose a Lessons", font=("Arial", 16))
        label.pack(pady=10)

        lesson_titles = [lesson.title for lesson in lessons.values()]
        lesson_var = tk.StringVar()
        lesson_var.set("Choose")  # Initialize with an empty string

        # Create a dropdown menu to select a lesson
        lesson_dropdown = tk.OptionMenu(lesson_window, lesson_var, *lesson_titles)
        lesson_dropdown.pack(pady=10)

        # Create a text widget to display lesson content
        lesson_content_text = tk.Text(lesson_window, font=("Arial", 12), height=10, width=40)
        lesson_content_text.pack(pady=10)
        lesson_content_text.config(state=tk.DISABLED)  # Disable text editing

        # Button to show lesson content
        show_content_button = tk.Button(lesson_window, text="Show Content", command=show_lesson_content)
        show_content_button.pack()

        lesson_window.mainloop()

if __name__ == "__main__":
    pass


    

