class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            minl = float('inf')
            for i in intervals:
                if i[0] <= q <= i[1]:
                    minl = min(minl, (i[1]- i[0]+1))
            res.append(minl if minl != float('inf') else -1)
        return res