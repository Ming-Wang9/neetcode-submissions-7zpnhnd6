class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        maxlen = 1
        sset = set()
        sset.add(s[l])
        for r in range(1,len(s)):
            while s[r] in sset:
                sset.remove(s[l]) 
                l+=1
            sset.add(s[r])
            maxlen = max(maxlen, r-l+1)
        return maxlen