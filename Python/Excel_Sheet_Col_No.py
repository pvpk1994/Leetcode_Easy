# Author: Pavan Kumar Paluri
# Excel Sheet Column Number

from string import ascii_uppercase
import math
class Solution:
    def __init__(self):
        self.hash_map = {}
    def titleToNumber(self, s: str) -> int:
        counter = 1
        for c in ascii_uppercase:
            # Populate the hashmap
            self.hash_map[c] = counter
            counter += 1
        if len(s) == 1:
            return self.hash_map[s]
        result = 0
        # Advanced cases
        for i in range(len(s)):
            result += self.hash_map[s[i]]*int(math.pow(26, len(s)-1-i))
        return result
 
