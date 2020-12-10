# Strictly Increasing and Strictly Decreasing Sequences in a Uni-Dimensional Array
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/valid-mountain-array/

#------------ My solution TC:O(N) and SC:O(1) -----------------------
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <3:
            return False
        else:
            bc = False
            threshold = 0
            for i in range(1, len(arr)):
                if arr[i-1]-arr[i] < 0:
                    continue
                elif arr[i-1] == arr[i]:
                    return False
                else:
                    threshold = i
                    bc = True
                    # print(threshold)
                    break
            if threshold >1 and bc:
                for l in range(threshold, len(arr)-1):
                    if arr[l]-arr[l+1] > 0:
                        continue
                    elif arr[l] == arr[l+1]:
                        return False
                    else:
                        return False
                return True
        return False
 
 #------------------ Efficient Solution (One Pass) -----------------------
 class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
