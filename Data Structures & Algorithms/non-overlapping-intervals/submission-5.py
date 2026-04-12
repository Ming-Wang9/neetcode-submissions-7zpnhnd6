class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0]) 
        curend = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < curend:
                res+=1
                curend = min(curend, intervals[i][1])
            else:
                curend=intervals[i][1]
        return res