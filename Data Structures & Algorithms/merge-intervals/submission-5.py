class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res =[]
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur[1]:
                cur = [min(cur[0], intervals[i][0]),
                        max(cur[1], intervals[i][1])]
            else:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res