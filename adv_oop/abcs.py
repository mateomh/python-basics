# ABCs implementation
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
  def walk(self):
    print('walking....')

  @abstractmethod
  def num_legs(self):
    # responsability of the child class to implement the method
    # kind of an interface
    pass


class Dog(Animal):
  def __init__(self, name):
    self.name = name

  def num_legs(self):
    return 4

class Monkey(Animal):
  def __init__(self, name):
    self.name = name

  def num_legs(self):
    return 2
  
animals = [Dog('blita'), Monkey('bubu')]

for animal in animals:
  if isinstance(animal, Animal):
    # if it is an instance of animal you know it has the num_legs method
    print(animal.num_legs())