from abc import ABCMeta, abstractmethod
from database import Database

# Super class, or abstract class or interface
# It is not an interface strictly speaking because it has functionality defined in it
class Saveable(metaclass=ABCMeta):
  def save_to_db(self):
    Database.insert(self.to_dict())

  @abstractmethod
  def to_dict(self):
    pass
