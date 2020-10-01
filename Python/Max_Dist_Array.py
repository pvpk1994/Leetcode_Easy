# Find the maximum distance between arrays in list of arrays
# Expected time complexity: O(N)
# Leetcode Question: https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for lister in arrays[1:]:
            result = max(result, max(abs(max_val-lister[0]), abs(lister[-1]-min_val)))
            min_val = min(min_val, lister[0])
            max_val = max(max_val, lister[-1])
        return result
