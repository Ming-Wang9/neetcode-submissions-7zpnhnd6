class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                lastidx, lasth = stack.pop()
                maxarea = max(maxarea, lasth*(i-lastidx))
                start = lastidx
            stack.append([start, h])
        n = len(heights)
        for i,h in stack:
            maxarea = max(maxarea, h*(n-i))
        return maxarea
