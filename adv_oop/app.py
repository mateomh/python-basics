from admin import Admin
from database import Database

a = Admin('ralf', '1234', 3)

a.save_to_db()

print(Database.content)
print(Database.find(lambda x: x['username'] == 'ralf'))
