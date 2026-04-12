class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        n = len(temperatures)
        res = [0] * n
        for i, t in enumerate(temperatures):
            while stack and t>temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i-idx
            stack.append(i)
        return res