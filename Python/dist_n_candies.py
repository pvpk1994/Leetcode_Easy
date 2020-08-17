# Problem Description: https://leetcode.com/problems/distribute-candies-to-people/
# Time Complexity: O(sqrt(N))
# Author: Pavan Kumar Paluri
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output = [0]*(num_people)
        candy = 1
        i = 0
        while candies > 0:
            output[i%num_people] += min(candies, candy)
            candies -= candy
            candy+=1
            i+=1
        return output
