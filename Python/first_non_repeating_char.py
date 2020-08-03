'''
Author: Pavan Kumar Paluri
Problem Description: 
--------------------
Find first non-repeating character in a given string
'''
def firstNotRepeatingCharacter(s):
    hash_set = []
    dup_list = []
    for character in s:
        if character not in hash_set:
            hash_set.append(character)
        else:
            dup_list.append(character)
             # if char is in hash_set?
    print(hash_set)
    for elem in hash_set:
        if elem not in dup_list:
            return elem
        else:
            continue
            
    return '_'
