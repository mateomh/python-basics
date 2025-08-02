# my_file = open('./data.txt', 'r')
# file_content = my_file.read()
# my_file.close()

# print(file_content)

# Module import
import files.file_operations as file_operations # module import

file_operations.save_to_file('Test', './data.txt')
content = file_operations.read_file('./data.txt')

print(content)

# Global name import
from files.file_operations import save_to_file, read_file

save_to_file('Test', './data.txt')
content = read_file('./data.txt')

print(content)

# Modules in another folder
# Absolute import
import utils.file_utils as file_utils
# from utils.file_utils import save_to_file, read_file

content = file_utils.read_file('./data.txt')
print(content)
