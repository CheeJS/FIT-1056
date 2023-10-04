# Third party imports
import tkinter as tk
from application_layer import Application  
from tkinter import *

class LearnerFrame(tk.Frame):


    def __init__(self, master, username=""):

        super().__init__(master=master)
        self.app_layer = Application(master)
        self.username = username
        # Label containing the welcome heading
        login_title = tk.Label(master=self,text="Learner Interface",font=("Arial Bold", 25))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        students_btn = Button(self, text="View Lesson", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                              fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.select_lesson())
        students_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        add_btn = Button(self, text="Attempt Quiz", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.select_quiz(self.username ))
        add_btn.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        view_student_btn = Button(self, text="View Grade", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.student_get_grade(self.username ))
        view_student_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        log_out_btn = Button(self, text="Log Out", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.logout())
        log_out_btn.grid(row=5, column=0, padx=10, pady=10, sticky="w")





if __name__ == "__main__":
    pass
