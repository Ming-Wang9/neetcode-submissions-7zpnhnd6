class Solution:
    def findMin(self, nums: List[int]) -> int:
        # question has already give me a hint
        # yes, binary search
        res = nums[0]
        l,r = 0, len(nums)-1
        while l <=r:
            #the array is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            m = l + (r-l)//2
            res = min(res, nums[m])
            #m is in the left sorted part, 
            #the min should on the right --> move l
            if nums[l] <= nums[m]:
                l = m+1
            #nums[m] < nums[l], mean the min landed between 
            #m and l --> move r 
            else:
                r = m-1
        return res

            
            
            
