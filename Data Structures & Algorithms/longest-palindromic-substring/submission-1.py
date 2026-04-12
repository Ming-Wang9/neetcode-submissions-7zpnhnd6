class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two point for sure
        # instead of starting from both side
        # starting from character itself and spread to both side
        residx = 0 
        maxlen = 0
        for i in range(len(s)):
            #odd lenth
            l, r= i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > maxlen:
                    maxlen = r-l+1
                    residx = l
                l -= 1
                r += 1
            #even length
            l,r=i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > maxlen:
                    maxlen = r-l+1
                    residx = l
                l -= 1
                r += 1
        return s[residx:residx+maxlen]
