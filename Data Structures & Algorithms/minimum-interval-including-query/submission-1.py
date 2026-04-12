class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        output = [-1] * n
        for i in range(n):
            res = float('inf')
            for j in range(len(intervals)):
                if intervals[j][0]<=queries[i]<=intervals[j][1]:
                    res=min(res, intervals[j][1]-intervals[j][0]+1)
            if res != float('inf'):
                output[i] = res
            else:
                output[i] = -1
        return output