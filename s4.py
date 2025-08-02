# OOP

class Student:
  # dunder method (dunder = double underscore)
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  def average(self):
    return sum(self.grades) / len(self.grades)
  
student1 = Student('Ralf', [70, 88, 90, 99])

print(student1.name)
print(student1.grades)
print(student1.average())
print(Student.average(student1))
print(student1)
print(student1.__class__)
print(['a', 'b'].__class__)
print("a".__class__)


# Special dunder methods
class Garage:
  def __init__(self):
    self.cars = []

  # This method allows to call len(garage_obj) on the object 
  def __len__(self):
    return len(self.cars)
  
  # This method allow to run indexing on the object garage_obj[i]
  def __getitem__(self, i):
    return self.cars[i]
  
  # This method gets called when using the debugger.
  # If the str dunder method is not defined this is what gets printed
  def __repr__(self):
    return f"<Garage {self.cars}>"
  
  # This method is called when printing the object print(garage_obj)
  def __str__(self):
    return f"Garage with {len(self)} cars."
  
garage1 = Garage()
garage1.cars.append('My car')
garage1.cars.append('Your car')
print(len(garage1))
print(garage1[0])
print(garage1)
print(garage1.__class__)

# Inheritance
class Student:
  # dunder method (dunder = double underscore)
  def __init__(self, name, grades, school):
    self.name = name
    self.grades = grades
    self.school = school

  def average(self):
    return sum(self.grades) / len(self.grades)
  
class WorkingStudent(Student):
  def __init__(self, name, grades, school, hourly_salary):
    super().__init__(name, grades, school)
    self.hourly_salary = hourly_salary

  def weekly_salary(self):
    return self.hourly_salary * 40

student1 = WorkingStudent('Ralf', [70, 88, 90, 99], "La Salle", 15.5)
print(student1.name)
print(student1.hourly_salary)
print(student1.school)
print(student1.average())
print(student1.weekly_salary())

# Property decorator. For methods that only take self as argument so you don't have to put brakets to call it
class Student:
  # dunder method (dunder = double underscore)
  def __init__(self, name, grades, school):
    self.name = name
    self.grades = grades
    self.school = school

  @property
  def average(self):
    return sum(self.grades) / len(self.grades)

student1 = Student('Ralf', [70, 88, 90, 99], 'La Salle')

print(student1.name)
print(student1.grades)
print(student1.average)

# classmethod and staticmethod decorators
class Student:
  # dunder method (dunder = double underscore)
  def __init__(self, name, grades, school):
    self.name = name
    self.grades = grades
    self.school = school

  @property
  def average(self):
    return sum(self.grades) / len(self.grades)
  
  # Receives the class instead of the object(self) as the first argument
  @classmethod
  def hi(klass):
    print(klass.__name__)

  @staticmethod
  def hello():
    print("doesn't takes any arguments from the object")
  
student1 = Student('Ralf', [70, 88, 90, 99], 'La Salle')

print(student1.name)
print(student1.grades)
print(student1.average)
print(student1.hi())
print(student1.hello())
