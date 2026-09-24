class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for c in s:
            sdict[c] = 1+sdict.get(c,0)
        tdict = {}
        for c in t:
            tdict[c] = 1+tdict.get(c,0)
        return sdict==tdict