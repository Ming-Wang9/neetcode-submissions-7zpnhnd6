"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if intervals:
            cur = intervals[0]
        else:
            return True
        for i in range(1, len(intervals)):
            if intervals[i].start < cur.end:
                return False
            cur = intervals[i]
        return True