class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            # all indiviuals are sorted
            if nums[l] <= nums[r]:
                return nums[l]
            #rotated
            m = l+(r-l)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return nums[l]
        
