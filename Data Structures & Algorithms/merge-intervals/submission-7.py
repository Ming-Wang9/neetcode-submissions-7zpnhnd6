class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort based on the start of an intervals
        intervals.sort(key = lambda x : x[0])
        res = []
        newinv = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= newinv[1]:
                newinv[1] =max([newinv[1], intervals[i][1]])
            else:
                res.append(newinv)
                newinv = intervals[i]
        res.append(newinv)
        return res