# Third party imports
import tkinter as tk
from application_layer import Application  
from tkinter import *


class TeacherFrame(tk.Frame):

    def __init__(self, master):
    
        super().__init__(master=master)
        self.app_layer = Application(master)
    
        # Label containing the welcome heading
        login_title = tk.Label(master=self,
                               text="Teacher Interface",
                               font=("Arial Bold", 25))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)


        view_student_grade_btn = Button(self, text="View students grade", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                              fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.teacher_get_all_students_grade())
        view_student_grade_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        add_student_btn = Button(self, text="Add Student", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.add_user(2))
        add_student_btn.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        view_all_student_btn = Button(self, text="View All Students", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.get_all_students())
        view_all_student_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        add_lesson_btn = Button(self, text="Add Lesson", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.add_lesson())
        add_lesson_btn.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        edit_lesson_btn = Button(self, text="Edit Lesson", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.edit_select_lesson())
        edit_lesson_btn.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        log_out_btn = Button(self, text="Log Out", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.logout())
        log_out_btn.grid(row=7, column=0, padx=10, pady=10, sticky="w")



if __name__ == "__main__":
    pass
