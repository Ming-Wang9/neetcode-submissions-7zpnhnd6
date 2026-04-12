class Solution:
    def isValid(self, s: str) -> bool:
        sdic = {"{" : "}","[" : "]", "(" : ")" }
        stack = []
        for c in s:
            if c in sdic:
                stack.append(c)
            else:
                if stack and c== sdic[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0