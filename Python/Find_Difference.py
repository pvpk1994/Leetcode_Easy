# Find the Difference between two given strings 
# Author: Pavan Kumar Paluri

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_map = collections.Counter(s)
        
        for character in t:
            if character not in hash_map.keys():
                return character
            elif character in hash_map.keys():
                hash_map[character]-=1
        for character in hash_map.keys():
            if hash_map[character]<0:
                return character
