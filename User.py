
class User:
  def __init__(self,fName,LName,username,password,role):
    self.firstname = fName
    self.lastname = LName
    self.username = username
    self.password = password
    self.role = role


  def get_first_name(self):
    return self.first_name

  def set_first_name(self, first_name):
    self.first_name = first_name

  def get_last_name(self):
    return self.last_name

  def set_last_name(self, last_name):
    self.last_name = last_name

  def get_username(self):
    return self.username

  def set_username(self, username):
    self.username = username

  def get_password(self):
    return self.password

  def set_password(self, password):
    self.password = password

  def get_role(self):
    return self.role

  def set_role(self, role):
    self.role = role

  def log_out(self):
    print("logging out")
