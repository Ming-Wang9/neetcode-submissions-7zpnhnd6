class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res =[0] * n
        stack = []
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        return res