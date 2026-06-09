class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for c in s:
            sdict[c] = 1+sdict.get(c,0)
        cdict = {}
        for c in t:
            if c not in sdict:
                return False
            cdict[c] = 1+cdict.get(c,0)
            if cdict[c] > sdict[c]:
                return False
        return sdict == cdict
            