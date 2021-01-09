# Add strings
# Time Complexity: O(N) and Space complexity:O(N)
# Leetcode Question: https://leetcode.com/problems/add-strings/
# Author: Pavan Kumar Paluri

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        final_ans =0
        p1 = len(num1)-1
        p2= len(num2)-1
        res =[]
        carry =0
        while p1>=0 or p2>=0:
            # ASC-II character 
            n1 = ord(num1[p1])-ord('0') if p1>=0 else 0
            n2 = ord(num2[p2])-ord('0') if p2>=0 else 0
            
            res.append((n1+n2+carry)%10)
            carry = (n1+n2+carry)//10
            p1-=1
            p2-=1
        if carry:
            res.append(carry)
        return ''.join([str(x) for x in res[::-1]])
