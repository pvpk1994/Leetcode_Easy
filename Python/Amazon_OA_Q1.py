# Given a string , find the sum of numbers in the string 
# Note; String can contain numbers (if digits are consecutive) 
# Expected Time Complexity: O(N) where N is the size of the string 
# Author: Pavan Kumar Paluri
def count_sum(string:str):
  temp  = ""
  final_sum = 0
  for char in string:
    if char.isdigit():
      temp += char
    else:
      if temp != "":
        final_sum += int(temp)
      temp = ""
  # if here:
  if temp !="":
    final_sum += int(temp)
    temp = ""
  return final_sum

if __name__ =="__main__":
  print(count_sum("13ba42"))
