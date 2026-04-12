class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isnorl(token):
            return (ord('A') <= ord(token) <= ord('Z') or
                    ord('a') <= ord(token) <= ord('z') or 
                    ord('0') <= ord(token) <= ord('9'))
        news = ""
        for c in s:
            if isnorl(c):
                news+=c.lower()
        l,r=0,len(news)-1
        while l <= r:
            if news[l] != news[r]:
                return False
            l+=1
            r-=1
        return True