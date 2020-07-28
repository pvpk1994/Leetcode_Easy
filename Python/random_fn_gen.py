# Find smallest two power larget than given number
# Implement random_128 Generator using random_01 generator
import math
import random

def smallest_two_power(num:int)->int:
  power = math.ceil(math.log2(num))
  # smallest_two_power = math.pow(2, power)
  return power

def random_128_gen(num:int)->int:
  two_power = smallest_two_power(num)
  st = ""
  for i in range(two_power):
    st += str(random_01_gen())
  # print(st)
  # Convert binary string to a decimal number
  result = int(st, 2)
  if(result > 128):
    random_128_gen(6)
  else:
    return result 


def random_01_gen()->int:
  return random.randint(0, 1)
if __name__ == "__main__":
  #print(int(smallest_two_power(39)))
  print(random_128_gen(128))
