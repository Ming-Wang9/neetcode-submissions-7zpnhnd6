class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left and right two point to track
        # width is  r -l
        # get the max((r-l) * heights[i]
        l, r = 0, len(heights)-1
        maxarea = 0
        availableheight = 0
        while l <r:
            availableheight = min(heights[l], heights[r])
            maxarea = max(maxarea, availableheight * (r-l))
            if heights[l]>heights[r]:
                r -= 1
            else:
                l+=1
        return maxarea

            
