class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = [] #(available index, height)
        maxarea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                lastidx,lasth = stack.pop()
                maxarea = max(maxarea, (i-lastidx)*lasth)
                start = lastidx
            stack.append([start,h])
        for i, h in stack:
            maxarea = max(maxarea, (len(heights)-i)*h)
        return maxarea