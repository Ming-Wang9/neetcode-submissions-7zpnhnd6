class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitdict = {"2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"kjl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        if not digits:
            return []
        res = []
        def backtrack(i,com):
            if i == len(digits):
                res.append(''.join(com))
                return
            for c in digitdict[digits[i]]:
                com.append(c)
                backtrack(i+1,com)
                com.pop()

        backtrack(0,[])
        return res





