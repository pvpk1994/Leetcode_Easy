# Find n smaller numbers than the n+1th number
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = sorted(nums)
        dict_nums = Counter(new_nums)
        counter = {}
        final_list=[]
        ans=0
        for key,val in dict_nums.items():
            counter[key] = ans
            ans += val
        for i in range(0,len(nums)):
            final_list.append(counter[nums[i]])
        return final_list 
   
