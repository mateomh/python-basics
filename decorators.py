#====================================================================
#* Simple decorator
"""
A decorator is a function that returns another function and takes one
function as an argument (higher order function)
"""
import functools


user = {'username': 'jose123', 'access_level': 'admin'}

def user_has_permissions(func):
  if user.get('access_level') == 'admin':
    return func
  raise RuntimeError

def a_function_to_pass():
  return 'Password for admin panel is 1234'

secure_function = user_has_permissions(a_function_to_pass)

print(secure_function())

# ======================================================================
#* @syntax for decorators
user = {'username': 'jose123', 'access_level': 'admin'}

# decorator
def user_has_permissions(func):
  def secure_func():
    """
    This is the secure func
    """
    if user.get('access_level') == 'admin':
      return func()
    raise RuntimeError
  
  return secure_func

# this way the function can't be called directly
# ties it to the decorator
@user_has_permissions
def a_function_to_pass():
  """
  This is the doc string for the original function
  """
  return 'Password for admin panel is 1234'

print(a_function_to_pass())
print(a_function_to_pass.__name__)
print(a_function_to_pass.__doc__)

# =====================================================================
#* The way to keep the name of the original function and the doc string
def user_has_permissions(func):
  @functools.wraps(func)
  def secure_func():
    """
    This is the secure func
    """
    if user.get('access_level') == 'admin':
      return func()
    raise RuntimeError
  
  return secure_func

# this way the function can't be called directly
# ties it to the decorator
@user_has_permissions
def a_function_to_pass():
  """
  This is the doc string for the original function
  """
  return 'Password for admin panel is 1234'

print(a_function_to_pass())
print(a_function_to_pass.__name__)
print(a_function_to_pass.__doc__)

# ======================================================================
#* Decorating functions that have parameters
def user_has_permissions(func):
  @functools.wraps(func)
  def secure_func(panel):
    """
    This is the secure func
    """
    if user.get('access_level') == 'admin':
      return func(panel)
    raise RuntimeError
  
  return secure_func

# this way the function can't be called directly
# ties it to the decorator
#! If done like this you can't apply the decorator to another function
@user_has_permissions
def a_function_to_pass(panel):
  """
  This is the doc string for the original function
  """
  return f'Password for {panel} panel is 1234'

print(a_function_to_pass('movies'))
print(a_function_to_pass.__name__)
print(a_function_to_pass.__doc__)

# ======================================================================
#* How to use decorators that take parameters
def user_has_permissions(access_level):
  def a_decorator(func):
    @functools.wraps(func)
    def secure_func(panel):
      """
      This is the secure func
      """
      if user.get('access_level') == access_level:
        return func(panel)
      raise RuntimeError
    
    return secure_func
  
  return a_decorator

# this way the function can't be called directly
# ties it to the decorator
@user_has_permissions('admin')
def a_function_to_pass(panel):
  """
  This is the doc string for the original function
  """
  return f'Password for {panel} panel is 1234'

def another_function_to_decorate():
  pass

print(a_function_to_pass('movies'))
print(a_function_to_pass.__name__)
print(a_function_to_pass.__doc__)


# ======================================================================
#* Functions that accept any number of arguments
def add_all(*args):
  # args are passed a a tuple and the order is the order the arguments have
  print(args)
  return sum(args)

def pretty_print(**kwargs):
  # kwargs are passed as a dictionary of named arguments
  # the key is the name and the value is the value
  for key, value in kwargs.items():
    print(f"For {key} we have {value}")

add_all(1,2,3,4,5)
pretty_print(username='jose', access_level='admin')
pretty_print(**{'username': 'jose', 'access_level': 'admin'})

# ====================================================================
#* Making the decorator generic for any function
def user_has_permissions(access_level):
  def a_decorator(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
      """
      This is the secure func
      """
      if user.get('access_level') == access_level:
        return func(*args, **kwargs)
    
    return secure_func
  
  return a_decorator

# this way the function can't be called directly
# ties it to the decorator
@user_has_permissions('admin')
def a_function_to_pass(panel):
  """
  This is the doc string for the original function
  """
  return f'Password for {panel} panel is 1234'

@user_has_permissions('user')
def another_function_to_decorate():
  return f"This is another function"

print(a_function_to_pass('movies'))
print(another_function_to_decorate())
print(a_function_to_pass.__name__)
print(a_function_to_pass.__doc__)