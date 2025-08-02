import sqlite3

class DatabaseConnection:
  def __init__(self, database_file):
    self.connection = None
    self.database_file = database_file

  def __enter__(self) -> sqlite3.Connection:
    self.connection = sqlite3.connect(self.database_file)
    return self.connection

  def __exit__(self, exc_type, exc_val, exc_tb):
    # exc_type: Exception type
    # exc_val: Exception value
    # exc_tb: Exception trace back
    if exc_type or exc_val or exc_tb:
      self.connection.close()
    else:
      self.connection.commit()
      self.connection.close()