class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"}":"{", ")":"(", "]":"["}
        stack = []
        for c in s:
            if c not in bracket: #open bracket
                stack.append(c)
            else:  
                if stack and bracket[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

