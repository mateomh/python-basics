from typing import Union

def divide(dividend: Union[int, float], divisor: Union[int, float]):
  if divisor == 0:
    raise ValueError
  
  return dividend / divisor

def multiply(*args: Union[int, float]):
  if len(args) == 0:
    raise ValueError('At least one value must be passed')
  
  total = 1.0
  for arg in args:
    total *= arg

  return total