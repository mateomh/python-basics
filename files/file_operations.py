def save_to_file(content, file_name):
  # Context manager (with)
  with open(file_name, 'w') as file:
    file.write(content)

def read_file(file_name):
  # Context manager (with)
  with open(file_name, 'r') as file:
    return file.read()
