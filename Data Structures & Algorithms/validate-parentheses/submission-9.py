class Solution:
    def isValid(self, s: str) -> bool:
        sdic ={
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        for c in s:
            if c in sdic:
                if not stack or sdic[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0