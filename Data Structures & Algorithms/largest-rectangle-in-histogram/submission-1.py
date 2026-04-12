class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # stores (index, height)

        for i, h in enumerate(heights + [0]):  # add sentinel 0
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index  # extend start to the leftmost popped bar
            stack.append((start, h))
        return maxArea
