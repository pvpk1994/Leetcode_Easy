# Squares of sorted array 
# Author: Pavan Kumar Paluri
# Leetcode Easy - https://leetcode.com/problems/squares-of-a-sorted-array/
# Time Complexity: O(N) and Space O(N) (No sorting required)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        output = [None for _ in range(0, len(nums))]
        start = 0
        end = len(nums)-1
        i = end
        while start <= end:
            if nums[start]*nums[start] > nums[end]*nums[end]:
                output[i] = nums[start]*nums[start]
                start+= 1
                i-=1
            else:
                output[i] = nums[end]*nums[end]
                end-=1
                i-=1
        # if here: list should be complete
        return output
        
