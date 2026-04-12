class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0 
        l, r = 0, len(height)-1
        l_max = height[l]
        r_max = height[r]
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                if l_max - height[l] >=0:
                    count += l_max-height[l]
            else:
                r -= 1
                r_max =max(r_max, height[r])
                if r_max - height[r] >= 0:
                    count += r_max-height[r]
        return count
        