class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l) //2
            if nums[m] == target:
                return m 
            #m in left part
            if nums[l] <= nums[m]:
                #target is in this range
                if nums[l] <= target < nums[m]:
                    r = m -1
                else:
                    l = m+1
            #m in the right part 
            # elif  nums[l] > nums[m]:
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1
                
               
            
