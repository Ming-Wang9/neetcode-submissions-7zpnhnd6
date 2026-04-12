class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res =[]
        start = newInterval[0]
        end = newInterval[1]
        for i in range(len(intervals)):
            if end < intervals[i][0]:
                res.append([start,end])
                return res + intervals[i:]
            #if it not overlap, the new start larger than the end
            elif start > intervals[i][1]:
                res.append(intervals[i])
            #if overlap, merge
            else:
                start = min(intervals[i][0],start)
                end = max(intervals[i][1],end)
        res.append([start,end])
        return res


