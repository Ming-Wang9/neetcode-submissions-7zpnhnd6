class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search????
        l = 1
        res = r = max(piles)
        while l <= r:
            m = l+(r-l)//2
            totaltime = 0
            for p in piles:
                if p % m != 0:
                    totaltime += 1+p//m
                else:
                    totaltime += p//m
            if totaltime > h:
                l = m+1
            if totaltime <= h:
                res = min(res, m)
                r=m-1 
        return res




                