# Running Sum problem 
# Author: Pavan Kumar Paluri
# Time Complexity: O(N) and Space: O(1) - Constant space

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # in constant space without creating a new array
        # Time complexity: O(N) and Space: O(1)
        for i in range(1, len(nums)):
            nums[i] = nums[i]+nums[i-1]
        return nums
