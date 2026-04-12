class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtoc = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def backtrack(i,curstr):
            if len(curstr) == len(digits):
                res.append("".join(curstr))
                return
            for c in dtoc[digits[i]]:
                curstr.append(c)
                backtrack(i+1,curstr)
                curstr.pop()
            return res
        if not digits:
            return []
        return backtrack(0,[])
        



            