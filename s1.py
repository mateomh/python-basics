# Constants
PI = 3.14159

# integer division
integer_division = 12 // 3
print(integer_division)
float_division = 12 / 3
print(float_division)

# multiline strings
multiline = """Line 1
Line2
Line3
"""
print(multiline)

# converting to string
num_as_string = str(34)
print("The number is " + num_as_string)

# formating strings (interpolating)
num = 34
test_string = f"The number is: {num}"
print(test_string)

template_string = "The number is:: {}"
test_string = template_string.format(num)
print(test_string)
num = 35
test_string2 = template_string.format(num)
print(test_string2)

template_string = "The number is:: {num}"
test_string = template_string.format(num=num)
print(test_string)
num = 37
test_string2 = template_string.format(num=num)
print(test_string2)

# getting user input
# my_name = 'test'
# your_name = input('Enter your name: ')
# print(f'Hello {your_name}, my name is {my_name}')

# age = input('Enter your age: ')
# age = int(age)
# print(f'You have lived for {age * 12} months')

# Lists (Arrays)
friends = ['friend1', 'friend2', "friend3"]
print(len(friends))
friends.append('friend4')
print(friends)
friends.remove('friend2')
print(friends)

friends = [['friend1', 1],['friend2', 3],['friend3', 34]]
print(friends[0][0])

# Tuples (immutable lists, can't add elements to them)
short_tuple = 'friend1', 'friend2'
clearer_tuple = ('friend1', 'friend2')
tuple_in_list = [('friend1', 1), ('friend2', 3), ('friend3', 34)]
print(short_tuple)
print(clearer_tuple)
print(tuple_in_list)
friends = ('friend1', 'friend2')
friends_plus = friends + ('friend3',)
print(friends)
print(friends[1])
print(friends_plus)

# Sets (doesn't hold order)
friends = {'friend1', 'friend2', 'friend3'}
friends.add('friend4')
print(friends)
friends.remove('friend2')
print(friends)

friends1 = {'friend1', 'friend2'}
friends2 = {'friend4', 'friend2', 'friend3'}

not_in_both = friends1.symmetric_difference(friends2)
diff1 = friends1.difference(friends2)
diff2 = friends2.difference(friends1)
in_both = friends1.intersection(friends2)
all_friends = friends1.union(friends2)

print(diff1)
print(diff2)
print(in_both)
print(not_in_both)
print(all_friends)

# Dictionaries (Hashes or objects)
person_ages = {"person1": 24, "person2": 30, "person3": 50}
print(person_ages["person2"])

persons = [("person1", 24), ("person2", 30), ("person3", 50)]
persons_dictionary = dict(persons) # makes it the same as person_ages
print(persons_dictionary)

# Length and Sum
grades = [80, 75, 90, 100]
total = sum(grades)
count = len(grades)
average = total / count
print(average)

