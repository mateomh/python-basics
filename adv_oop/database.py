class Database:
  content = { 'users': [] } # class variable

  @classmethod
  def insert(klass, data):
    klass.content['users'].append(data)

  @classmethod
  def remove(klass, finder_func):
    klass.content['users'] = [user for user in klass.content['users'] if not finder_func(user)]

  @classmethod
  def find(klass, finder_func):
    # finder_func can be lambda x: x['username'] == 'test'
    return [user for user in klass.content['users'] if finder_func(user)]
