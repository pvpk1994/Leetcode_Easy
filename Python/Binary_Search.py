# Time Complexity: O(logN)
# Author: Pavan Kumar Paluri
# Simple Binary Search 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] < target:
                # search the right part
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                # nums[mid]==target
                return mid
        return -1
