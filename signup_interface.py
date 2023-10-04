# Third party imports
import tkinter as tk
from Student import Student

# Local application imports
from application_layer import Application
class SignUpFrame(tk.Frame):
    """
    The class definition for the SignUpFrame class.
    """
    def __init__(self, master):
        super().__init__(master=master)
        self.app_layer = Application(master)


    def signUp(self):
        
        def validate():
            firstName= first_name_entry.get()
            lastName= last_name_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            if (firstName=="" or lastName=="" or username=="" or password=="" ):
                tk.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty!")
            else:
                student = Student(fName=firstName,lName=lastName,username=username,password=password)
                self.app_layer.students[username] = student
                self.app_layer.update_user_data(student)
                tk.messagebox.showinfo('Success Message',"Successfully registered!")
        add_user_window = tk.Toplevel()
        add_user_window.title("Sign Up")
        add_user_window.geometry(f"{500}x{500}")


        sign_up_label = tk.Label(add_user_window, text="Sign Up",width=20,font=("bold", 20))
        sign_up_label.place(x=90,y=53)

        first_name_label = tk.Label(add_user_window, text="First Name",width=20,font=("bold", 10))
        first_name_label.place(x=80,y=130)

        first_name_entry = tk.Entry(add_user_window)
        first_name_entry.place(x=240,y=130)

        last_name_label = tk.Label(add_user_window, text="Last Name",width=20,font=("bold", 10))
        last_name_label.place(x=80,y=180)

        last_name_entry = tk.Entry(add_user_window)
        last_name_entry.place(x=240,y=180)

        username_label = tk.Label(add_user_window, text="Username",width=20,font=("bold", 10))
        username_label.place(x=80,y=230)

        username_entry = tk.Entry(add_user_window)
        username_entry.place(x=240,y=230)

        password_label = tk.Label(add_user_window, text="Password",width=20,font=("bold", 10))
        password_label.place(x=80,y=280)

        password_entry = tk.Entry(add_user_window, show="●")
        password_entry.place(x=240,y=280)

        add_student_button = tk.Button(add_user_window, text='Submit', width=20, bg='green', fg='white',command=lambda: validate())
        add_student_button.place(x=180, y=380)




if __name__ == "__main__":
    pass
