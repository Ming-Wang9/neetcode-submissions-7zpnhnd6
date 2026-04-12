class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        prod = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            prod_list.append(prod)
            prod = 1
        return prod_list
        