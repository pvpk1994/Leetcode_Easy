'''
Author: Pavan Kumar Paluri
Problem Description:
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.

Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.

Example 3:

Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.
'''

import math
class Solution:
    def binaryGap(self, N: int) -> int:
        # COnvert a number into a binary 
        bin_str = "{0:b}".format(N)
        # FInd all 1s in this string
        list_1s =[num for (num, e) in enumerate(bin_str) if e=='1']
        # iterate through the string
        max_num = -math.inf
        if list_1s is None or len(list_1s)==1:
            return 0
        for i in range(len(list_1s)-1):
            if list_1s[i+1]-list_1s[i] > max_num:
                max_num = list_1s[i+1]-list_1s[i]
            else:
                continue
        return max_num
