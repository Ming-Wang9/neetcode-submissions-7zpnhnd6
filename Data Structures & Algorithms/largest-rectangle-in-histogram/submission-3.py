class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  #[height, index]
        maxrec = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h <=stack[-1][0]:
                last_h, last_i = stack.pop()
                maxrec = max(maxrec, last_h*(i-last_i))
                start = last_i
            stack.append([h,start])

        n = len(heights)
        for h, i in stack:
            maxrec = max(maxrec, h*(n-i))
            
        return maxrec