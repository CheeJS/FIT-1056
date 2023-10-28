'''
This file defines the AdminFrame class, which represents the graphical user interface for the admin user
It allows the admin to perform actions such as adding students and teachers, and viewing all students and teachers
'''

# Third party imports
import tkinter as tk
#from week09_interface import Interface
from tkinter import *
from application_layer import Application
#from login_interface import LoginFrame  




class AdminFrame(tk.Frame):
    def __init__(self, master,login_frame):
        """
        Initialises the AdminFrame and sets up the user interface components.
        Parameters:
        master (tk.Tk or tk.Toplevel): The parent window or frame
        app (Application): An instance of the Application class that handles application logic
        username (str): The username of the admin user
        """
        super().__init__(master=master)

        self.app_layer = Application(master)
        # Label containing the welcome heading
        login_title = tk.Label(self, text="Admin Interface", font=("Arial Bold", 25))
        login_title.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Button to Add student
        students_btn = Button(self, text="Add Students", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                              fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.add_user(2))
        students_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Button to Add Teacher
        add_btn = Button(self, text="Add Teachers", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.add_user(1))
        add_btn.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        # Button to view all Student
        view_student_btn = Button(self, text="View All Students", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.get_all_students())
        view_student_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Button to view all Teacher
        view_teacher_btn = Button(self, text="View All Teachers", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.get_all_teachers())
        view_teacher_btn.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Button to log out
        log_out_btn = Button(self, text="Log Out", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.logout())
        log_out_btn.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        # Button to quit whole application
        quit_btn = Button(self, text="Quit Game", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                         fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',command=lambda: self.app_layer.quit())
        quit_btn.grid(row=7, column=0, padx=10, pady=10, sticky="w")

if __name__ == "__main__":
    pass

