'''
This file shows the opening interface. 
The interface class is created to state the welcome message and set the geometry of the interface.
'''
# Third party imports
import tkinter as tk
from admin_interface import AdminFrame
from learner_interface import LearnerFrame

# Local application imports
from login_interface import LoginFrame
from teacher_interface import TeacherFrame

#Class for opening interface, sets geometry
class Interface(tk.Tk):
    """
    Class definition for the Interface class
    """
    def __init__(self, title, width=960, height=540):
        """
        Constructor for the Interface class,
        the main window for the HCMS.
        :param title: str
        :param width: int - default 960 pixels
        :param height: int - default 540 pixels
        """
        self.width = width
        self.height = height
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")  # Set the window geometry
        self.login_frame = LoginFrame(self)
        self.admin_frame = AdminFrame(self,self.login_frame)
        self.learner_frame = LearnerFrame(self)
        self.teacher_frame = TeacherFrame(self)

        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.login_frame.master = self  

    def run(self):
        self.mainloop()
        
    def show_login_frame(self):
        self.admin_frame.pack_forget()  # Hide the admin frame if it's visible
        self.learner_frame.pack_forget() 
        self.teacher_frame.pack_forget() 
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


#Sets the text that is displayed and where
if __name__ == "__main__":
    codeventure = Interface("Welcome to the CodeVenture Learning Program")
    #login = LoginFrame(codeventure)
    #login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    codeventure.run()
    print("--- End of program execution ---")
