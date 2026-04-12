class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(strs):
            l,r=0,len(strs)-1
            while l<=r:
                if strs[l]!=strs[r]:
                    return False
                l+=1
                r-=1
            return True
        maxlen = 0
        res =[]
        for l in range(len(s)):
            for r in range(l,len(s)):
                if isPali(s[l:r+1]):
                    if r-l+1>=maxlen:
                        maxlen = r-l+1
                        res = s[l:r+1]
        return res
