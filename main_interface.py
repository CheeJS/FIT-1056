'''
This file shows the opening interface. 
The interface class is created to state the welcome message and set the geometry of the interface.
'''
# Third party imports
import tkinter as tk

# Local application imports
from login_interface import LoginFrame
from application_layer import Application

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

#Sets the text that is displayed and where
if __name__ == "__main__":
    codeventure = Interface("Welcome to the CodeVenture Learning Program")
    app = Application(codeventure.width,codeventure.height)
    login = LoginFrame(codeventure,app)
    login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    codeventure.mainloop()
    print("--- End of program execution ---")
