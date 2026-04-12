class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Step 1: sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        res = []
        new = intervals[0]

        # Step 2: iterate and merge
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new[1]:
                # Overlapping — merge
                new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]
            else:
                # No overlap — push the merged interval
                res.append(new)
                new = intervals[i]
        
        # Step 3: append last interval
        res.append(new)
        return res
