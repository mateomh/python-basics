class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def __repr__(self):
    return f"<USer {self.username}>"

  def login(self):
    return 'Logged in!'
