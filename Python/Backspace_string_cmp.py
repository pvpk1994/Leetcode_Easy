# Author: Pavan Kumar Paluri
# Backspace String Comparison

class Solution:
    def remove_at(self,i, s):
        return s[:i] + s[i+1:]
    
    def final_str(self,S: str):
        while S.count("#") >0:
            finder = S.find("#")
            if finder > 0:
                S = self.remove_at(finder, S)
                S = self.remove_at(finder-1, S)
            elif finder==0:
                S=self.remove_at(finder, S)
        return S
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.final_str(S)== self.final_str(T)
 
