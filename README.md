The code flow by starting at main_interface to login_interface

In login interface we determine what is the role of the user either(Admin,Student,Teacher)

Then we create the user interface based on User's role

All the main features implemented in application_layer, all the feature from all the user are in application_layer.

If anywhere requires data, like application_layer requires data, it will retreives data from the (user_data.txt,lesson_data,quiz_data_title.py,quiz_data.py). We can consider
this as the database layer