class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        new_s = ''
        for c in s:
            if alphaNum(c):
                new_s+=c.lower()

        l,r = 0, len(new_s)-1
        while l <= r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True


