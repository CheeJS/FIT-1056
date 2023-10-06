'''
This module defines the LoginFrame class, which represents the login interface for the CodeVenture learning program
'''

# Third party imports
import tkinter as tk

# Local application imports
from authenticator import Authenticator
from application_layer import Application
from signup_interface import SignUpFrame
class LoginFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """

    def __init__(self, master):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.app_layer = Application(master)
        self.signup_interface = SignUpFrame(master)
        self.auth = Authenticator()
        
        # Logo image for the login page
        login_canvas = tk.Canvas(master=self, width=128, height=128)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)


        image_path = "./images/python.png"
        self.login_logo = tk.PhotoImage(file=image_path)
        login_canvas.create_image(0, 0,
                                  anchor=tk.NW,
                                  image=self.login_logo)

        # Label containing the welcome heading
        login_title = tk.Label(master=self,
                               text="Welcome to the "
                                    "CodeVenture learning program",
                               font=("Arial Bold", 25))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Label to ask user for Username
        username_label = tk.Label(master=self, text="Username:")
        username_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and input widget for username
        self.username = tk.StringVar()


        # Add Entry widget for Username
        self.username_entry = tk.Entry(master=self, textvariable=self.username)
        self.username_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)  # Stick to the left

        # Label to ask user for Password
        password_label = tk.Label(master=self, text="Password:")
        password_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and input widget for password
        self.password = tk.StringVar()

        # Add Entry widget for Password with hidden characters
        self.password_entry = tk.Entry(master=self, textvariable=self.password, show="●")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)  # Stick to the left


        # Button to login
        login_button = tk.Button(master=self, text="Login",
                                 command=self.authenticate_login)
        login_button.grid(row=4, columnspan=2, padx=10, pady=10)


        self.login_text = tk.StringVar()
        self.login_outcome_label = tk.Label(master=self, textvariable=self.login_text, font=("Arial", 12))
        self.login_outcome_label.grid(row=6, columnspan=2, padx=10, pady=10, sticky=tk.N)  # Centered

         # Button to Sign Up
        sign_up = tk.Button(master=self, text="Sign Up", command=lambda:self.app_layer.add_user(2))
        sign_up.grid(row=5, columnspan=3, padx=10, pady=10)
        
        
    def authenticate_login(self):
        """
        Authenticate the user's login credentials and open the appropriate interface based on their role.
        """
        if self.auth.authenticate(self.username.get(),self.password.get()):   
            username = self.username.get()   
            password =  self.password.get()
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0,tk.END)    
            self.place_forget()                                            
            role = self.auth.authenticate_get_role(username, password)
            if role == "AD":
                interface = self.master.admin_frame
            elif role == "TA":
                interface = self.master.teacher_frame
            elif role == "LR":
                self.master.learner_frame.username = username
                interface = self.master.learner_frame
            
            interface.grid(row=0, column=0, rowspan=2, sticky="nsew")  
            interface.grid_columnconfigure(0, weight=1)  
            interface.pack(side="left", fill="both")  

        else:
            self.login_text.set("Failed to login")



if __name__ == "__main__":
    pass
