# Third party imports
import tkinter as tk

# Local application imports
from week09_loginframe import LoginFrame
from application_layer import Application


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


if __name__ == "__main__":
    hcms = Interface("Health Clinic Management System")
    app = Application(hcms.width,hcms.height)
    login = LoginFrame(hcms,app)
    login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    hcms.mainloop()
    print("--- End of program execution ---")
