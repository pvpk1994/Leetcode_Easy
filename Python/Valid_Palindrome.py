# Author: Pavan Kumar Paluri
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert everything into lower cases
        s = s.lower()
        s = s.replace(" ", "")
        # print(s)
        # punctuation marks 
        # "`l;`` 1o1 ??;l`"
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        
        for char in s:
            if char in punctuations:
                s=s.replace(char, "")
        
        # print(s)
        low = 0
        high = len(s)-1
        while(low<=high):
            if s[low]==s[high]:
                low+=1
                high-=1
            else:
                return False
        return True
