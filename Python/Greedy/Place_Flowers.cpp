# Place Flowers 
# Author: Pavan kumar Paluri
# Leetcode Question: https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        counter =0
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i]==1:
                continue
            else:
                if flowerbed[i-1]+flowerbed[i+1]==0:
                    # alternate places are 0
                    flowerbed[i]=1
                    counter+=1
        return True if counter >= n else False
