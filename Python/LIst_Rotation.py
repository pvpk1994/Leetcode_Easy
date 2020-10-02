# Rotate Array 
# Author: Pavan Kumar Paluri
# Leetcode: https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # list rotation
        new_nums=[]
        for i in range(0, len(nums)):
            new_nums.append(nums[i])
        for i in range(0, len(nums)):
            nums[(i+k)%len(nums)]=new_nums[i]
