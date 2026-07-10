class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        def isPali(string):
            l,r=0,len(string)-1
            while l<=r:
                if string[l]!=string[r]:
                    return False
                l+=1
                r-=1
            return True
        res = []
        def backtrack(i,sub):
            if i == len(s):
                res.append(sub.copy())
                return
            for j in range(i,len(s)):
                if isPali(s[i:j+1]):
                    sub.append(s[i:j+1])
                    backtrack(j+1,sub)
                    sub.pop()
        backtrack(0,[])
        return res