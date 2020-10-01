# Number of recent calls 
# Using queue
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/number-of-recent-calls/

from collections import deque
# iteration over sliding window 
class RecentCounter:

    def __init__(self):
        self.requests=deque([])
        
    def ping(self, t: int) -> int:
        low = t-3000
        high = t
        self.requests.append(t)
        while self.requests:
            if self.requests[0]<low:
                # if so
                self.requests.popleft()
            else:
                break
        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
