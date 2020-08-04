# Author: Pavan Kumar Paluri
# Find the power of 4 for a given 32-bit signed integer 
import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        if math.log2(num)%2==0:
            return True
        return False 
