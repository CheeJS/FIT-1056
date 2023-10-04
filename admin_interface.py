# Third party imports
import tkinter as tk
#from week09_interface import Interface
from tkinter import *
from application_layer import Application
#from login_interface import LoginFrame  




class AdminFrame(tk.Frame):

    def __init__(self, master,login_frame):
        super().__init__(master=master)

        self.app_layer = Application(master)
        # Label containing the welcome heading
        login_title = tk.Label(self, text="Admin Interface", font=("Arial Bold", 25))
        login_title.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        students_btn = Button(self, text="Add Students", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                              fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.add_user(2))
        students_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        add_btn = Button(self, text="Add Teachers", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.add_user(1))
        add_btn.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        view_student_btn = Button(self, text="View All Students", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.get_all_students())
        view_student_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        view_teacher_btn = Button(self, text="View All Teachers", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.get_all_teachers())
        view_teacher_btn.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        log_out_btn = Button(self, text="Log Out", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.logout())
        log_out_btn.grid(row=6, column=0, padx=10, pady=10, sticky="w")


if __name__ == "__main__":
    pass

