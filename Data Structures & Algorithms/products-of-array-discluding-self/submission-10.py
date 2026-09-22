class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # prefix = [1] * n
        # suffix = [1] * n
        # res = [1] * n
        # for i in range(1,n):
        #     prefix[i] = prefix[i-1]*nums[i-1]
        # for j in range(n-2,-1,-1):
        #     suffix[j] = suffix[j+1]*nums[j+1]
        # for k in range(n):
        #     res[k] = prefix[k]*suffix[k]
        # return res
        n = len(nums)
        res = [1] * n 
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix*=nums[i]
        suffix = 1
        for j in range(n-1,-1,-1):
            res[j] *= suffix
            suffix*=nums[j]
        return res

        