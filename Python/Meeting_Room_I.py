# Meeting Rooms 
# Author: Pavan Kumar Paluri
# Leetcode-Easy

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)==0:
            return True
        intervals = sorted(intervals, key = lambda x: x[0])
        y0 = intervals[0][1]
        for i in range(1, len(intervals)):
            if y0<=intervals[i][0]:
                y0=intervals[i][1]
                continue
            else:
                return False 
        return True 
