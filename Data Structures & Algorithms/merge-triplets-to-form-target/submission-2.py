class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res =[float('-inf'), float('-inf'), float('-inf')]
        for t in triplets:
            if (t[0] > target[0] or 
                t[1] > target[1] or 
                t[2] > target[2]):
                continue
            for i in range(3):
                res[i] = max(res[i], t[i])
        if res == target:
            return True
        return False