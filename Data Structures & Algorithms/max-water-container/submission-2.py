class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left and right two point to track
        # width is  r -l
        # get the max((r-l) * heights[i]
        l, r = 0, len(heights)-1
        maxarea = 0
        availableheight = 0
        while l <r:
            if heights[l]>heights[r]:
                availableheight = heights[r]
                maxarea = max(maxarea, availableheight * (r-l))
                r -= 1
            else:
                availableheight = heights[l]
                maxarea = max(maxarea, availableheight * (r-l))
                l+=1
        return maxarea

            
