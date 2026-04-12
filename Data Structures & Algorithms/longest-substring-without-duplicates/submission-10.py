class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding windows
        char = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            maxlen = max(maxlen, r-l+1)
        return maxlen