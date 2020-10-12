# Buddy Strings
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        if A==B:
            seen = set()
            for char in A:
                if char in seen:
                    return True
                seen.add(char)
            return False
        elif A!=B:
            pair_list = []
            for a,b in zip(A,B):
                if a!=b:
                    pair_list.append((a,b))
            if len(pair_list)>=3:
                return False
            if len(pair_list)==2:
                if pair_list[0]==pair_list[1][::-1]:
                    return True
                else:
                    return False 
