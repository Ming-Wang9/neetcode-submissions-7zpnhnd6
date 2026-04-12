class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=float('inf')
        while l<=r:
            #current range of array is sorted
            if nums[l]<=nums[r]:
                res=min(res, nums[l])
            m=l+(r-l)//2
            res=min(res,nums[m])
            #search lands on left part, min is in right side of m
            if nums[l] <= nums[m]:
                l=m+1
            #search lands on right part, min is on the left side of m
            #if nums[m] < nums[0]:
            else:
                r=m-1
        return res
