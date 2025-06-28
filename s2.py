# Conditionals
def s2_conditionals():
  person = "Test1"
  user_person = input("Enter your name: ")

  if user_person == person:
    print("Hello person")
  else:
    print("Not a person")

  friends = ("friend1", 'friend2', 'friend3')
  family = ('family1', 'family2')

  if user_person in friends:
    print('You are a friend')
  elif user_person in family:
    print('You are family')
  else:
    print("Stranger!!!!")

# While loops
def s2_while_loops():
  is_running = True
  while is_running:
    print("it is running")
    user_input = input("Do you want to keep it running: ")
    is_running = user_input == 'yes'

# For loops
def s2_for_loops():
  friends = ("friend1", 'friend2', 'friend3')
  for friend in friends:
    print(friend)

  for _ in friends:
    print("test")

  for index in range(3):
    print("same test")

# Destructuring
def s2_destructuring():
  friends = ("friend1", 'friend2', 'friend3')
  f1, f2, _ = friends
  print(f1)
  print(f2)

  persons = [("person1", 24), ("person2", 30), ("person3", 50)]
  for name, age in persons:
    print(name)
    print(age)

# Iterating over dictionaries
def s2_dictionary_iteration():
  person_ages = {"person1": 24, "person2": 30, "person3": 50}

  for key, value in person_ages.items():
    print(key)
    print(value)

# Else in loops
def s2_else_in_loops():
  cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok', 'ok']

  for status in cars:
    if status == 'faulty':
      print("Stopping!!!!")
      break
    print(f"The car is {status}")
  else:
    print("All cars were ok, no faulty cars")

  # finding prime numbers
  for n in range(2,10):
    for x in range(2, n):
      if n%x == 0:
        print(f"{n} is not a prime")
        break
    else:
      print(f"{n} is a prime number")

# Slicing
def s2_slicing_lists():
  friends = ("friend1", 'friend2', 'friend3')
  print(friends[1:3])
  print(friends[1:])
  print(friends[-2:])
  print(friends[-1])
  print(friends[:2])

# List comprehensions (map)
def s2_comprehensions():
  numbers = [0,1,2,3,4]
  doubled_numbers = [number*2 for number in numbers]
  print(numbers)
  print(doubled_numbers)

  # Comprehensions with conditionals
  ages = [22,35,27,21,20]
  odd_ages = [age for age in ages if age%2 == 1]

  print(odd_ages)

# Enumerate
def s2_enumerate():
  friends = ("friend1", 'friend2', 'friend3')

  for index, friend in enumerate(friends):
    print(index)
    print(friend)

  print(list(enumerate(friends)))

# Lambda functions (one line functions)
def s2_lambda_functions():
  # lambda functions take inputs and return outputs
  # 
  divide = lambda x, y: x / y
  print(divide(5,2))

  students = [
    {"name": "Bob", "grades": (67,90,95,100)},
    {"name": "Ralf", "grades": (56,78,80,90)},
    {"name": "Jen", "grades": (98,90,95,99)},
    {"name": "Anne", "grades": (100,100,95,100)},
  ]

  average = lambda sequence: sum(sequence) / len(sequence)

  for student in students:
    print(average(student["grades"]))

# First Class functions
def s2_first_class_functions():
  average = lambda sequence: sum(sequence) / len(sequence)
  total = lambda seq: sum(seq)
  top = lambda seq: max(seq)

  operations = {
    "average": average,
    "total": total,
    "top": top
  }

  students = [
    {"name": "Bob", "grades": (67,90,95,100)},
    {"name": "Ralf", "grades": (56,78,80,90)},
    {"name": "Jen", "grades": (98,90,95,99)},
    {"name": "Anne", "grades": (100,100,95,100)},
  ]

  for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    op = input("Enter average, total or top: ")
    print(operations[op](grades))
