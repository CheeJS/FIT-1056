import os
from re import X
from tkinter import DISABLED, END, RIDGE, W, Button, Checkbutton, Entry, IntVar, Label, OptionMenu, Radiobutton, Scrollbar, StringVar, Toplevel, messagebox, Toplevel, messagebox,E,Text
import tkinter
from tracemalloc import Frame
from Admin import Admin
from Student import Student
from Teacher import Teacher
import tkinter as tk
from random import choice
from tkinter.ttk import Treeview
from tkinter import ttk
from quiz_data import quiz_data
from tkinter.ttk import Combobox  
from quiz_data_title import quiz_data_title
import shutil



class Application:
    def __init__(self,width,height):
        # Initialize any necessary resources or settings here
        self.width = width
        self.height = height
        self.file_path = "./data/user_data.txt"
        self.lesson_data_path = "./lesson_data/"
        self.all_users = {}
        self.students = {}
        self.teachers = {}
        self.admins = {}
        self.load_users()
        self.current_question = 0
        self.score = 0
        self.quiz_scores = {}
        self.quiz_options = quiz_data_title
        self.questions = quiz_data



    def add_student(self):
        
        def validate():
            firstName= entry_1.get()
            lastName= entry_2.get()
            username = entry_3.get()
            password = entry_4.get()
            if (firstName=="" or lastName=="" or username=="" or password=="" ):
                tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty!")
            else:
                self.students[username] = Student(fName=firstName,lName=lastName,username=username,password=password)
                tkinter.messagebox.showinfo('Success Message',"Successfully registered!")
        add_student_window = tk.Toplevel()
        add_student_window.title("Add Student")
        add_student_window.geometry(f"{500}x{500}")


        label_0 = tk.Label(add_student_window, text="Add Student form",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        label_1 = tk.Label(add_student_window, text="First Name",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)

        entry_1 = tk.Entry(add_student_window)
        entry_1.place(x=240,y=130)

        label_2 = tk.Label(add_student_window, text="Last Name",width=20,font=("bold", 10))
        label_2.place(x=80,y=180)

        entry_2 = tk.Entry(add_student_window)
        entry_2.place(x=240,y=180)

        label_3 = tk.Label(add_student_window, text="Username",width=20,font=("bold", 10))
        label_3.place(x=80,y=230)

        entry_3 = tk.Entry(add_student_window)
        entry_3.place(x=240,y=230)

        label_4 = tk.Label(add_student_window, text="Password",width=20,font=("bold", 10))
        label_4.place(x=80,y=280)

        entry_4 = tk.Entry(add_student_window, show="●")
        entry_4.place(x=240,y=280)

        add_student_button = Button(add_student_window, text='Submit', width=20, bg='green', fg='white',command=lambda: validate())
        add_student_button.place(x=180, y=380)

    def select_quiz(self,username):
        quiz_window = Toplevel()
        quiz_window.title("Select Quiz")
        quiz_window.geometry(f"{350}x{150}")

        label = Label(quiz_window, text="Select Quiz:", width=20, font=("bold", 10))
        label.place(x=20, y=30)



        quiz_combobox = Combobox(quiz_window, values=self.quiz_options ,state="readonly")
        quiz_combobox.place(x=140, y=30)
        quiz_combobox.set(self.quiz_options[0])

        def start_quiz():
            selected_quiz_index = quiz_combobox.current()  # Get the selected index
            selected_quiz_name = self.quiz_options [selected_quiz_index]  # Get the quiz name using the index
            messagebox.showinfo("Selected Quiz", f"You selected: {selected_quiz_name} (Index: {selected_quiz_index})")
            quiz_window.destroy()
            self.start_quiz(index=selected_quiz_index,username=username)
        quiz_button = Button(quiz_window, text='Start Quiz', width=10, bg='green', fg='white',
                         command=start_quiz)
        quiz_button.place(x=110, y=80)






    
    def select_lesson(self):
        lesson_window = Toplevel()
        lesson_window.title("Select Lesson")
        lesson_window.geometry(f"{350}x{150}")

        label = Label(lesson_window, text="Select Lesson:", width=20, font=("bold", 10))
        label.place(x=20, y=30)

        # List of lessons, replace this with your actual lesson names
        lesson_options = sorted(os.listdir(self.lesson_data_path))
        selected_lesson = tk.StringVar(value=lesson_options[0])
        lesson_combobox = tk.OptionMenu(lesson_window, selected_lesson, *lesson_options)
        lesson_combobox.place(x=150, y=30)

        def start_lesson():
            selected_lesson_name = selected_lesson.get()
            lesson_window.destroy()
            self.start_lesson(selected_lesson_name)

        lesson_button = Button(lesson_window, text='Start Lesson', width=10, bg='green', fg='white',
                               command=start_lesson)
        lesson_button.place(x=110, y=80)

    def start_lesson(self, selected_lesson_name):
        lesson_folder_path = os.path.join(self.lesson_data_path, selected_lesson_name)
        lesson_files = sorted(os.listdir(lesson_folder_path))
        current_file_index = 0
        self.display_lesson(lesson_files, current_file_index, selected_lesson_name)

    def start_edit_lesson(self, selected_lesson_name):
        lesson_folder_path = os.path.join(self.lesson_data_path, selected_lesson_name)
        lesson_files = sorted(os.listdir(lesson_folder_path))
        current_file_index = 0
        self.display_edit_lesson(lesson_files, current_file_index, selected_lesson_name)

    def display_edit_lesson(self, lesson_files, current_file_index, selected_lesson_name):
        if current_file_index < len(lesson_files):
            lesson_file = lesson_files[current_file_index]
            lesson_window = tk.Toplevel()
            lesson_window.title("Lesson")
            lesson_window.geometry(f"{self.width}x{self.height}")

            name, _ = os.path.splitext(lesson_files[current_file_index])
            folder_name_label = tk.Label(lesson_window,
                   text=name,
                   font=("Arial Bold", 25))
            folder_name_label.grid(row=1, columnspan=3, padx=10, pady=10)  # Use columnspan to span all three columns

            lesson_text = tk.Text(lesson_window, wrap=tk.WORD, font=('Verdana', 12), height=20, width=90)  # Adjust height and width here
            lesson_text.grid(row=2, column=0, padx=10, pady=10, columnspan=3)  # Span all three columns

            scrollbar = tk.Scrollbar(lesson_window)
            scrollbar.grid(row=2, column=3, sticky='ns')  # Adjust the column
            lesson_text.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=lesson_text.yview)

            with open(os.path.join(self.lesson_data_path, selected_lesson_name, lesson_file), "r", encoding="utf-8") as file:
                lesson_content = file.read()
                lesson_text.insert(tk.END, lesson_content)
                lesson_text.config(state=tk.NORMAL)  # Allow editing

            save_button = tk.Button(lesson_window, text='Save', width=10, command=lambda: self.save_lesson_changes(
            lesson_text, selected_lesson_name, lesson_file))
            save_button.grid(row=3, column=0, padx=10, pady=10)  # Use row 3, adjust padx and pady

            back_button = tk.Button(lesson_window, text='Back', width=10, command=lambda: self.display_previous_edit_lesson(
            lesson_files, current_file_index, selected_lesson_name, lesson_window))
            back_button.grid(row=3, column=1, padx=10, pady=10)  # Use row 3, adjust padx and pady

            next_button = tk.Button(lesson_window, text='Next', width=10, command=lambda: self.display_next_edit_lesson(
            lesson_files, current_file_index, selected_lesson_name, lesson_window))
            next_button.grid(row=3, column=2, padx=10, pady=10)  # Use row 3, adjust padx and pady

            if current_file_index == len(lesson_files) - 1:
                end_label = tk.Label(lesson_window, text="End of Lesson", font=("bold", 14))
                end_label.grid(row=4, column=0, columnspan=3, pady=10)  # Span all three columns

            return lesson_window



    def save_lesson_changes(self, lesson_text, selected_lesson_name, lesson_file):
        edited_content = lesson_text.get("1.0", tk.END)  # Get the edited content from the Text widget
        lesson_path = os.path.join(self.lesson_data_path, selected_lesson_name, lesson_file)
        with open(lesson_path, "w", encoding="utf-8") as file:
            file.write(edited_content)
        lesson_text.config(state=tk.DISABLED)  # Disable editing after saving

    def display_lesson(self, lesson_files, current_file_index, selected_lesson_name):
        if current_file_index < len(lesson_files):
            lesson_file = lesson_files[current_file_index]
            lesson_window = tk.Toplevel()
            lesson_window.title("Lesson")
            lesson_window.geometry(f"{self.width}x{self.height}")

            name, _ = os.path.splitext(lesson_files[current_file_index])
            folder_name_label = tk.Label(lesson_window,
                           text=name,
                           font=("Arial Bold", 25))
            folder_name_label.grid(row=1, columnspan=2, padx=10, pady=10)

            lesson_text = tk.Text(lesson_window, wrap=tk.WORD, font=('Verdana', 12), height=20, width=90)  # Adjust height and width here
            lesson_text.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

            scrollbar = tk.Scrollbar(lesson_window)
            scrollbar.grid(row=2, column=2, sticky='ns')
            lesson_text.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=lesson_text.yview)

            with open(os.path.join(self.lesson_data_path, selected_lesson_name, lesson_file), "r", encoding="utf-8") as file:
                lesson_content = file.read()
                lesson_text.insert(tk.END, lesson_content)
                lesson_text.config(state=tk.DISABLED)

            if current_file_index == len(lesson_files) - 1:
                end_label = tk.Label(lesson_window, text="End of Lesson", font=("bold", 14))
                end_label.grid(row=3, column=0, columnspan=2, pady=10)

            back_button = tk.Button(lesson_window, text='Back', width=10, command=lambda: self.display_previous_lesson(
            lesson_files, current_file_index, selected_lesson_name, lesson_window))
            back_button.grid(row=4, column=0, pady=10)

            next_button = tk.Button(lesson_window, text='Next', width=10, command=lambda: self.display_next_lesson(
            lesson_files, current_file_index, selected_lesson_name, lesson_window))
            next_button.grid(row=4, column=1, pady=10)

            return lesson_window
    def display_next_edit_lesson(self, lesson_files, current_file_index, selected_lesson_name, lesson_window):
        lesson_window.destroy()
        current_file_index += 1
        self.display_edit_lesson(lesson_files, current_file_index, selected_lesson_name)

    def display_next_lesson(self, lesson_files, current_file_index, selected_lesson_name, lesson_window):
        lesson_window.destroy()
        current_file_index += 1
        self.display_lesson(lesson_files, current_file_index, selected_lesson_name)
    
    def display_previous_edit_lesson(self, lesson_files, current_file_index, selected_lesson_name, lesson_window):
        previous_index = current_file_index - 1
        if previous_index >= 0:
            lesson_window.destroy()  # Close the current lesson window
            self.display_edit_lesson(lesson_files, previous_index, selected_lesson_name)
    
    def display_previous_lesson(self, lesson_files, current_file_index, selected_lesson_name, lesson_window):
        previous_index = current_file_index - 1
        if previous_index >= 0:
            lesson_window.destroy()  # Close the current lesson window
            self.display_lesson(lesson_files, previous_index, selected_lesson_name)
    
    def start_quiz(self,index,username):
        # Create a new window for the quiz
        quiz_window = tk.Toplevel()
        quiz_window.title("Quiz")
        quiz_window.geometry(f"{self.width}x{self.height}")

        # Define the quiz variables
        questions = self.questions[index]
        total_questions = len(questions)
        self.current_question = 0
        self.score = 0

        # Create quiz elements
        question_label = tk.Label(quiz_window, height=5, width=28, bg='grey', fg="#fff",
                              font=('Verdana', 20), wraplength=500)
        question_label.pack(pady=10)

        v1 = StringVar(quiz_window)
        v2 = StringVar(quiz_window)
        v3 = StringVar(quiz_window)
        v4 = StringVar(quiz_window)

        option1 = tk.Radiobutton(quiz_window, textvariable=v1, bg="#fff", variable=v1, font=('Verdana', 20),
                            command=lambda: check_answer(questions, self.current_question, 0, self.score))
        option2 = tk.Radiobutton(quiz_window, textvariable=v2, bg="#fff", variable=v2, font=('Verdana', 20),
                            command=lambda: check_answer(questions, self.current_question, 1, self.score))
        option3 = tk.Radiobutton(quiz_window, textvariable=v3, bg="#fff", variable=v3, font=('Verdana', 20),
                            command=lambda: check_answer(questions, self.current_question, 2, self.score))
        option4 = tk.Radiobutton(quiz_window, textvariable=v4, bg="#fff", variable=v4, font=('Verdana', 20),
                            command=lambda: check_answer(questions, self.current_question, 3, self.score))

        option1.pack(pady=5)
        option2.pack(pady=5)
        option3.pack(pady=5)
        option4.pack(pady=5)

        button_next = tk.Button(quiz_window, text='Next', bg='Orange', font=('Verdana', 20),
                            command=lambda: next_question(questions, quiz_window, self.current_question, total_questions, self.score))
        button_next.pack(pady=10)
        user_ob = self.students[username]
        # Function to disable radio buttons
        def disable_buttons(state):
            option1['state'] = state
            option2['state'] = state
            option3['state'] = state
            option4['state'] = state

        # Function to check the selected answer
        def check_answer(questions, current_question, selected_option, score):
            selected_choice = questions[current_question]['choices'][selected_option]
            if selected_choice == questions[current_question]['answer']:
                self.score += 1
           
            disable_buttons('disable')
            button_next['state'] = 'normal'

        # Function to display the next question
        def next_question(questions, quiz_window, current_question, total_questions, score):
            if self.current_question < total_questions - 1:
                self.current_question += 1
                question_label.config(text=questions[self.current_question]['question'])

                # Set the options for the current question
                options = questions[self.current_question]['choices']

                v1.set(options[0])
                v2.set(options[1])
                v3.set(options[2])
                v4.set(options[3])

                disable_buttons('normal')
                button_next['state'] = 'disabled'
            else:
                user_ob.all_quizzes[index] = self.score
                user_ob.attempted_quizzes[index] = True
                messagebox.showinfo("Quiz Completed", f"Quiz Completed! Final score: {self.score}/{total_questions}")
                print(user_ob.all_quizzes)
                quiz_window.destroy()

        # Start the quiz
        question_label.config(text=questions[self.current_question]['question'])

        # Set the options for the first question
        options = questions[self.current_question]['choices']
        v1.set(options[0])
        v2.set(options[1])
        v3.set(options[2])
        v4.set(options[3])

        disable_buttons('normal')



    def load_users(self):
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
                        self.admins[username] = user_obj
                    elif role == "TA":
                        user_obj = Teacher(fName=fName,lName=lName,username=username,password=password,role=role,is_active=bool(is_active))
                        self.teachers[username] = user_obj
                    elif role == "LR":
                        user_obj = Student(fName=fName,lName=lName,username=username,password=password,role=role,is_active=bool(is_active))
                        self.students[username] = user_obj
                    self.all_users[username] = user_obj
            return True
        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist!")
            return False
        
    
    def add_teacher(self):
        def validate():
            firstName= entry_1.get()
            lastName= entry_2.get()
            username = entry_3.get()
            password = entry_4.get()
            if (firstName=="" or lastName=="" or username=="" or password=="" ):
                tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty!")
            else:
                self.teachers[username] = Teacher(fName=firstName,lName=lastName,username=username,password=password)
                tkinter.messagebox.showinfo('Success Message',"Successfully registered!")
        add_student_window = tk.Toplevel()
        add_student_window.title("Add Student")
        add_student_window.geometry(f"{500}x{500}")


        label_0 = tk.Label(add_student_window, text="Add Teacher form",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        label_1 = tk.Label(add_student_window, text="First Name",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)

        entry_1 = tk.Entry(add_student_window)
        entry_1.place(x=240,y=130)

        label_2 = tk.Label(add_student_window, text="Last Name",width=20,font=("bold", 10))
        label_2.place(x=80,y=180)

        entry_2 = tk.Entry(add_student_window)
        entry_2.place(x=240,y=180)

        label_3 = tk.Label(add_student_window, text="Username",width=20,font=("bold", 10))
        label_3.place(x=80,y=230)

        entry_3 = tk.Entry(add_student_window)
        entry_3.place(x=240,y=230)

        label_4 = tk.Label(add_student_window, text="Password",width=20,font=("bold", 10))
        label_4.place(x=80,y=280)

        entry_4 = tk.Entry(add_student_window, show="●")
        entry_4.place(x=240,y=280)

        add_student_button = Button(add_student_window, text='Submit', width=20, bg='green', fg='white',command=lambda: validate())
        add_student_button.place(x=180, y=380)


    def edit_select_lesson(self):
        edit_select_lesson = Toplevel()
        edit_select_lesson.title("Edit Lesson")
        edit_select_lesson.geometry(f"{350}x{150}")

        label = Label(edit_select_lesson, text="Edit Lesson:", width=20, font=("bold", 10))
        label.place(x=20, y=30)

        # List of lessons, replace this with your actual lesson names
        lesson_options = sorted(os.listdir(self.lesson_data_path))
        selected_lesson = tk.StringVar(value=lesson_options[0])
        lesson_combobox = tk.OptionMenu(edit_select_lesson, selected_lesson, *lesson_options)
        lesson_combobox.place(x=150, y=30)

        def edit_lesson():
            selected_lesson_name = selected_lesson.get()
            edit_select_lesson.destroy()
            self.start_edit_lesson(selected_lesson_name)

        lesson_button = Button(edit_select_lesson, text='Edit', width=10, bg='green', fg='white',
                               command=edit_lesson)
        lesson_button.place(x=110, y=80)

    def add_lesson(self):
        def create_folder():
            folder_name = folder_name_entry.get()

            if not folder_name:
                messagebox.showerror("Error", "Folder name cannot be empty.")
                return

            folder_path = os.path.join(self.lesson_data_path, folder_name)

            if os.path.exists(folder_path):
                messagebox.showerror("Error", f"Folder '{folder_name}' already exists.")
                return

            try:
                os.makedirs(folder_path)
                lesson_index.set(1)  # Initialize lesson index

                # Create an entry for lesson name
                lesson_name_entry = Entry(add_lesson_window)
                lesson_name_entry.pack()

                create_lesson_file()
                folder_name_entry.config(state="disabled")  # Disable folder name entry
                create_button.config(state="disabled")  # Disable create button
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        def create_lesson_file():
            nonlocal lesson_index
            lesson_num = lesson_index.get()
            lesson_window = Toplevel()
            lesson_window.title(f"Add Lesson {lesson_num}")
            lesson_window.geometry(f"{self.width}x{self.height}")

            lesson_name_label = Label(lesson_window, text=f"Lesson {lesson_num} Name:")
            lesson_name_label.pack()
            lesson_name_entry = Entry(lesson_window)
            lesson_name_entry.pack()

            lesson_content_label = Label(lesson_window, text=f"Lesson {lesson_num} Content:")
            lesson_content_label.pack()
            lesson_content_text = Text(lesson_window, height=20, width=200)
            lesson_content_text.pack()

            def save_lesson():
                name = lesson_name_entry.get()
                content = lesson_content_text.get("1.0", "end-1c")
                if not name and not content:
                    messagebox.showerror("Error", "Lesson name cannot be empty.")
                    return
                folder_path = os.path.join(self.lesson_data_path, folder_name_entry.get())
                lesson_file_name = f"{name}.txt"
                lesson_file_path = os.path.join(folder_path, lesson_file_name)
                with open(lesson_file_path, "w") as lesson_file:
                    lesson_file.write(content)
                lesson_window.destroy()
                lesson_index.set(lesson_num + 1)
                create_lesson_file()

            def end_creation():
                #add_lesson_window.destroy()
                lesson_window.destroy()
                if folder_name_entry["state"] == "disabled":
                    # Folder was created during the lesson creation process
                    folder_path = os.path.join(self.lesson_data_path, folder_name_entry.get())
                    if not os.listdir(folder_path):
                    # If the folder is empty, delete it
                        try:
                            shutil.rmtree(folder_path)
                        except Exception as e:
                            messagebox.showerror("Error", f"Failed to delete the folder: {str(e)}")
                add_lesson_window.destroy()
                folder_name_entry.config(state="normal")  # Enable folder name entry
                create_button.config(state="normal")  # Enable create button

            save_button = Button(lesson_window, text="Save Lesson", command=save_lesson)
            save_button.pack()

            end_button = Button(lesson_window, text="End Creation", command=end_creation)
            end_button.pack()

        add_lesson_window = Toplevel()
        add_lesson_window.title("Add Lesson")
        add_lesson_window.geometry("400x200")

        folder_name_label = Label(add_lesson_window, text="Folder Name:")
        folder_name_label.pack()
        folder_name_entry = Entry(add_lesson_window)
        folder_name_entry.pack()

        create_button = Button(add_lesson_window, text="Create Folder", command=create_folder)
        create_button.pack()

        lesson_index = tk.IntVar()


    def teacher_get_all_students_grade(self):
        # Create a Toplevel window for displaying teacher information
        window = tk.Toplevel()
        window.title("Students' Grade Information")
        window.geometry(f"{self.width}x{self.height}")

        # Frame for search box and label
        search_frame = tk.Frame(window)
        search_frame.pack(padx=10, pady=5)

        # Label for the search box
        search_label = tk.Label(search_frame, text="Search by username:")
        search_label.pack(side='left')

        # Entry widget for searching
        search_entry = tk.Entry(search_frame)
        search_entry.pack(side='left', fill='x')

        table = Treeview(window, columns=('quiz_title', 'grade'), show='headings')
        table.heading('quiz_title', text='Quiz Title')
        table.heading('grade', text='Grade')
        table.pack(fill='both', expand=True)

        # Function to update the table based on the search query
        def update_table(search_query):
            table.delete(*table.get_children())  # Clear the existing rows

            if search_query in self.students:
                student = self.students[search_query]
                for i, quiz_title in enumerate(self.quiz_options):
                    grade = student.all_quizzes.get(i, 0)
                    str1 = str(grade) +"/"+ str(len(self.questions[i]))
                    data = (quiz_title, str1)
                    table.insert(parent='', index=tk.END, values=data)

        # Initial update of the table with all data
        update_table("")

        # Function to handle search box input
        def on_search_entry_change(event):
            search_query = search_entry.get()
            update_table(search_query)

        # Bind the search function to the Entry widget's text change event
        search_entry.bind("<KeyRelease>", on_search_entry_change)

        window.mainloop()

    def student_get_grade(self, username):
        # Create a Toplevel window for displaying teacher information
        window = tk.Toplevel()
        window.title("Grade Information")
        window.geometry(f"{self.width}x{self.height}")

        # Frame for search box and label
        search_frame = tk.Frame(window)
        search_frame.pack(padx=10, pady=5)

        # Label for the search box
        search_label = tk.Label(search_frame, text="Search by title:")
        search_label.pack(side='left')

        # Entry widget for searching
        search_entry = tk.Entry(search_frame)
        search_entry.pack(side='left', fill='x')

        table = Treeview(window, columns=('title', 'grade', 'attempt'), show='headings')
        table.heading('title', text='Quiz Title')
        table.heading('grade', text='Grade')
        table.heading('attempt', text='Attempted')
        table.pack(fill='both', expand=True)
        user_obj = self.students[username]

        # Function to update the table based on the search query
        def update_table(search_query):
            table.delete(*table.get_children())  # Clear the existing rows

            for i in range(len(self.quiz_options)):
                quiz_title = self.quiz_options[i]
                if search_query.lower() in quiz_title.lower():  # Case-insensitive search
                    if i in user_obj.all_quizzes:
                        str1 = str(user_obj.all_quizzes[i]) + "/" + str(len(self.questions[i]))
                        data = (quiz_title, str1, user_obj.attempted_quizzes[i])
                    else:
                        str1 = str(0) + "/" + str(len(self.questions[i]))
                        data = (quiz_title, str1, False)
                    table.insert(parent='', index=tk.END, values=data)

        # Initial update of the table with all data
        update_table("")

        # Function to handle search box input
        def on_search_entry_change(event):
            search_query = search_entry.get()
            update_table(search_query)

        # Bind the search function to the Entry widget's text change event
        search_entry.bind("<KeyRelease>", on_search_entry_change)

        window.mainloop()

    def get_all_teachers(self):
        def update_table(search_query):
            table.delete(*table.get_children())  # Clear the existing rows

            for teacher_id, teacher_info in self.teachers.items():
                user_obj = teacher_info
                if search_query.lower() in user_obj.get_username().lower():  # Case-insensitive search
                    data = (user_obj.get_firstName(), user_obj.get_lastName(), user_obj.get_username())
                    table.insert(parent='', index=tk.END, values=data)

        # Create a Toplevel window for displaying teacher information
        window = tk.Toplevel()
        window.title("Teacher Information")
        window.geometry(f"{self.width}x{self.height}")

        # Frame for search box and label
        search_frame = tk.Frame(window)
        search_frame.pack(padx=10, pady=5)

        # Label for the search box
        search_label = tk.Label(search_frame, text="Search by username:")
        search_label.pack(side='left')

        # Entry widget for searching
        search_entry = tk.Entry(search_frame)
        search_entry.pack(side='left', fill='x')

        table = Treeview(window, columns=('first', 'last', 'email'), show='headings')
        table.heading('first', text='First name')
        table.heading('last', text='Surname')
        table.heading('email', text='Email')
        table.pack(fill='both', expand=True)

        # Initial update of the table with all data
        update_table("")

        # Function to handle search box input
        def on_search_entry_change(event):
            search_query = search_entry.get()
            update_table(search_query)

        # Bind the search function to the Entry widget's text change event
        search_entry.bind("<KeyRelease>", on_search_entry_change)

        window.mainloop()




    def get_all_students(self):
        def on_close():
            window.destroy()

        # Create a Toplevel window for displaying student information
        window = tk.Toplevel()
        window.title("Student Information")
        window.geometry(f"{self.width}x{self.height}")
        table = Treeview(window, columns=('first', 'last', 'email'), show='headings')  # Use Treeview from ttk
        table.heading('first', text='First name')
        table.heading('last', text='Surname')
        table.heading('email', text='Email')
        table.pack(fill='both', expand=True)
    
        # Populate the Treeview with student information
        for student_id, student_info in self.students.items():
            user_obj = student_info 
            data = (user_obj.get_firstName(),user_obj.get_lastName(),user_obj.get_username())
            table.insert(parent='', index=tk.END, values=data)

        # Handle window close event
        window.protocol("WM_DELETE_WINDOW", on_close)

        window.mainloop()


