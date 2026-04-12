class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        new_interval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_interval[1]:
                new_interval[0] = min(intervals[i][0], new_interval[0])
                new_interval[1] = max(intervals[i][1], new_interval[1])
            else:
                res.append(new_interval)
                new_interval = intervals[i]
        res.append(new_interval)
        return res

