class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        leftmax, rightmax = height[l], height[r]
        water = 0
        while l<r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            if leftmax<rightmax:
                water+=leftmax-height[l]
                l+=1
            else:
                water+=rightmax-height[r]
                r-=1
        return water

