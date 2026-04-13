class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        k = r
        while l<=r:
            m = l+(r-l)//2
            hours = 0
            for p in piles:
                if p%m != 0:
                    hours+=1+p//m
                else:
                    hours+=p//m
            if hours > h:
                l=m+1
            else:
                k = min(k, m)
                r=m-1
        return k