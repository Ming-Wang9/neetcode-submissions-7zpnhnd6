class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            startindex = i
            while stack and h<= stack[-1][1]:
                lastindex, lastheight = stack.pop()
                res = max(res, (i-lastindex)*lastheight)
                startindex = lastindex
            stack.append([startindex,h])
        
        for i,h in stack:
            res= max(res,(len(heights)-i)*h)
        return res