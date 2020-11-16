# Determine whether a given string's any permutation of itself is a palindrome or not
# author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/palindrome-permutation/
# Using Hashmap : Time Complexity O(n), Space Complexity: O(1) - [Because, the number of distinct characters in the map as keys are limited in number]

from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        h_map = Counter(s)
        count = 0
        for val in h_map.values():
            count += val%2
        if count ==0 or count ==1:
            return True
        else:
            return False
