class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdic= {}
        for c in s:
            sdic[c] = 1+sdic.get(c,0)
        tdic ={}
        for c in t:
            tdic[c] = 1+tdic.get(c,0)
        return sdic == tdic