class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_1, map_2 = {}, {}
        for s in s1:
            map_1[s] = 1+ map_1.get(s, 0)
        
        l = 0
        for r in range(len(s2)):
            map_2[s2[r]] = 1+map_2.get(s2[r], 0)
            if (r-l+1) > len(s1):
                map_2[s2[l]] -= 1
                if map_2[s2[l]] == 0:
                    del map_2[s2[l]]
                l +=1
            if map_1 == map_2:
                return True
        return False

        