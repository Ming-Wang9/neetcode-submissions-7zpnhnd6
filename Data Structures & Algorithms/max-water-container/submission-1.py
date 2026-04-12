class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_rain = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            max_rain= max(max_rain, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        return max_rain