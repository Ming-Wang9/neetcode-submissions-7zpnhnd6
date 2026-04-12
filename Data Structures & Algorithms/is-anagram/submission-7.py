class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for c_s in s:
            count_s[c_s] = 1 + count_s.get(c_s, 0)
        for c_t in t:
            count_t[c_t] = 1 + count_t.get(c_t, 0)
        return count_s == count_t
            