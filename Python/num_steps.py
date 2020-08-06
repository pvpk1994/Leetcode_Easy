# Auhtor: Pavan Kumar Paluri
# Memoization - DP
'''
problem description:
-------------------
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        arr = [-1 for _ in range(n+1)]
        def helper(i , n, arr):
            
            if i==n:
                return 1
            if i > n:
                return 0
            if arr[i] != -1:
                return arr[i]
            
            arr[i]= helper(i+1, n, arr)+helper(i+2, n, arr)
            return arr[i]
        return helper(0, n, arr) 
            
