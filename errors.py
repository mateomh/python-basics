# Custom Error
# class MyCustomError(Exception):
#   """
#   (doc string)
#   Exception raise when an error with code is needed
#   """
  
#   def __init__(self, message, code):
#     super().__init__(f"Error Code: {code} - {message}")
#     self.code = code

#   def __repr__(self):
#     print(self.message)

# print(MyCustomError.__doc__)
# raise MyCustomError("This is an error", 450)

# Handling errors
class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

class Garage:
  def __init__(self):
    self.cars =[]

  def add_car(self, car):
    if not isinstance(car, Car):
      raise TypeError('Tried to add a {car.__class__.__name__} to the garage. You can only add "Car" type')
    self.cars.append(car)

garage = Garage()
car = Car('Ford', 'Fiesta')

garage.add_car(car)
try:
  garage.add_car('Fiesta')
except TypeError:
  print('This is not a car')
except ValueError:
  print('Something bad happened')
finally:
  # this always runs
  print('this always runs no matter if there was an error or not')

# On success and re-raising errors
class User:
  def __init__(self, name, engagement):
    self.name = name
    self.engagement_metrics = engagement

  def __repr__(self):
    return f"<User {self.name}>"

def email_engaged_user(user):
  try:
    user.score = perform_calculation(user.engagement_metrics)
  except KeyError:
    print('Incorrect values provided to the calculation function')
    raise # this re-raises the error
  else:
    # this runs if an error doesn't happen
    if user.score > 500:
      send_engagement_notification(user)

def perform_calculation(metrics):
  return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
  print(f"Notification sent to {user}")

my_user = User('Ralf', {'click': 500, 'hits': 200})
email_engaged_user(my_user)