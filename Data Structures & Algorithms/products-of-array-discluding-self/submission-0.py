class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        pre = pro = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            output[i] *= pro
            pro *= nums[i]
        return output