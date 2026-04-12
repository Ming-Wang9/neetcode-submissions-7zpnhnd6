class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < cur[1]:
                count += 1
                if intervals[i][1] < cur[1]:
                    cur = intervals[i]
            else:
                cur = intervals[i]
        return count 