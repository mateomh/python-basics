# __init__.py file is for compliance with older python versions
def save_to_file(content, file_name):
  # Context manager (with)
  with open(file_name, 'w') as file:
    file.write(content)

def read_file(file_name):
  # Context manager (with)
  with open(file_name, 'r') as file:
    return file.read()

# Name of the file assigned by python different when running it stand alone vs as module
# As stand alone is always __main__
print(__name__)

if __name__ == '__main__':
  print("code to test the module")