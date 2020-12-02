# Leetcode Question: https://leetcode.com/problems/shortest-word-distance/
# Author: Pavan Kumar Paluri

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        min_dist = math.inf
        a,b = math.inf, math.inf 
        for i in range(0, len(words)):
            if word1 == words[i]:
                a = i
                min_dist = min(min_dist, abs(a-b))
            if word2 == words[i]:
                b = i
                min_dist = min(min_dist, abs(a-b))
        return min_dist
