"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        res = 0
        maxres = 0
        s, e = 0, 0 
        while s < len(start):
            if start[s] < end[e]:
                res+=1
                s+=1
            else:
                res-=1
                e+=1
            maxres = max(maxres, res)
        return maxres