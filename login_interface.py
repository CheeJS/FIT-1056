


# Third party imports
import tkinter as tk

# Local application imports
from authenticator import Authenticator
from learner_interface import LearnerFrame
from admin_interface import AdminFrame
from teacher_interface import TeacherFrame
from application_layer import Application 


class LoginFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """

    def __init__(self, master,app):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.app_layer =  app

        # Logo image for the login page
        login_canvas = tk.Canvas(master=self, width=128, height=128)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)


        image_path = "./images/week09_image.png"
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

        


    def authenticate_login(self):
        authenticator = Authenticator()
        if authenticator.authenticate(self.username.get(),
                                  self.password.get()):
            self.destroy()  # Destroy the login frame
            if authenticator.authenticate_get_role(self.username.get(), self.password.get()) == "AD":
                interface = AdminFrame(self.master,self.app_layer,self.username.get())
            elif authenticator.authenticate_get_role(self.username.get(), self.password.get()) == "TA":
                interface = TeacherFrame(self.master,self.app_layer,self.username.get())
            elif authenticator.authenticate_get_role(self.username.get(), self.password.get()) == "LR":
                interface = LearnerFrame(self.master,self.app_layer,self.username.get())

            interface.grid(row=0, column=0, rowspan=2, sticky="nsew")  # Make the interface span two rows
            interface.grid_columnconfigure(0, weight=1)  # Make column 0 expand to fill available space
            interface.pack(side="left", fill="both")  # Display and align to the left

        else:
            self.login_text.set("Failed to login")



if __name__ == "__main__":

    pass
