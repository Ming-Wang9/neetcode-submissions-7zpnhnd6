class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        self.res = []
        def backtrack(o,c,pair):
            if o==c== n:
                self.res.append(pair)
                return 
            if o<n:
                backtrack(o+1,c,pair+"(")
            if c<o:
                backtrack(o,c+1,pair+")")
        backtrack(0,0,"")
        return self.res
