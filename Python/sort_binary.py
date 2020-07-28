# Segregate 0s and 1s in an array by only traversing once through the array 
# Traverse through the array only once. 
from collections import Counter 

def array_sort(arr:list)->list:
  # Make a dict 
  output= []
  dict_arr = Counter(arr)
  for key,val in dict_arr.items():
    for _ in range(val):
      output.append(key)
  return output

if __name__=="__main__":
  print(array_sort([0,0,1,1,0,1,0,0]))
