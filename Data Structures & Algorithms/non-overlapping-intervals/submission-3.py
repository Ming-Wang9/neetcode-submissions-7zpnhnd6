class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort by the ending value
        intervals.sort(key=lambda x: x[1])
        lastend = intervals[0][1]
        removecount = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < lastend:
                removecount += 1
            else:
                lastend = intervals[i][1]
        return removecount
            

