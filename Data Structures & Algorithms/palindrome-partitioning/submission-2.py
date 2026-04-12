class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(strs):
            if len(strs) == 1:
                return True
            l,r = 0,len(strs)-1
            while l<=r:
                if strs[l]!=strs[r]:
                    return False
                l+=1
                r-=1
            return True
        res=[]
        sub=[]
        def backtrack(i):
            if i == len(s):
                res.append(sub.copy())
                return
            for j in range(i,len(s)):
                if isPali(s[i:j+1]):
                    sub.append(s[i:j+1])
                    backtrack(j+1)
                    sub.pop()
        
        backtrack(0)
        return res




        