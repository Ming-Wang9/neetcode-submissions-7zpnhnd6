class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map, s2map = {}, {}
        for c1 in s1:
            s1map[c1] = 1+s1map.get(c1,0)
        l=0
        for r in range(len(s2)):
            s2map[s2[r]] = 1+s2map.get(s2[r], 0)
            if (r-l+1)>len(s1):
                s2map[s2[l]] -=1
                if s2map[s2[l]] == 0:
                    del s2map[s2[l]]
                l+=1
            if s2map==s1map:
                return True
        return False