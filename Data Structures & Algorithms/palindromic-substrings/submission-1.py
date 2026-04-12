class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def isPal(w):
            l,r= 0, len(w)-1
            while l<r:
                if w[l]!=w[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True
        for i in range(len(s)):
            for j in range(i,len(s)):
                if isPal(s[i:j+1]):
                    res += 1
        return res 
