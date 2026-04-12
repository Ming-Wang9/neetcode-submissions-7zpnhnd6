class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                res=nums[i+1]
        return res
