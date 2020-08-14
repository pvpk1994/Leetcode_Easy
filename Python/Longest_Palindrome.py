# Find the Length of longest possible palindrome possible 
# Author: Pavan Kumar Paluri
'''
Problem Description
-------------------
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

'''
from collections import Counter
class Solution:
    def __init__(self):
        self.max_len = 0
    def longestPalindrome(self, s: str) -> int:
        s_dict = Counter(s)
        ans = 0
        for val in s_dict.values():
            ans += (val//2)*2
            if ans%2==0 and val%2==1:
                ans += 1
        return ans 
