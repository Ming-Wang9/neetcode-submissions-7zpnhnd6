class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # (index, height)

        for i, h in enumerate(heights + [0]):  # Add sentinel
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                width = i if not stack else i - stack[-1][0] - 1
                maxArea = max(maxArea, height * width)
            stack.append((i, h))

        return maxArea
