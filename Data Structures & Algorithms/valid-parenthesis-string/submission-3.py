class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star =[]
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == "*":
                star.append(i)
            else: #c is )
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while stack and star:
            if stack.pop() > star.pop():
                return False
        return len(stack) == 0
        
