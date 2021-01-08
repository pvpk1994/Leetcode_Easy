# Check if two arrays are equivalant
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/solution/
# Time complexity: O(N) and Space Complexity: O(N)

# TC: O(N) and SC:O(N)
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ''.join([p for p in word1])
        str2 = ''.join([q for q in word2])
        return str1==str2
