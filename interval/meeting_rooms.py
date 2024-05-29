"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for inter in intervals[1:]:
            if inter.start < res[-1].end:
                # print(res[i-1].start, res[i-1].end)
                return False
            else:
                res.append(inter)
        print(res[-1].start, res[-1].end)  
        return True
