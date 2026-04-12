"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        i,j= 0,0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        rooms = 0
        maxrooms = 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                rooms+=1
                i+=1
            else:
                rooms-=1
                j+=1
            maxrooms = max(maxrooms, rooms)
        return maxrooms
