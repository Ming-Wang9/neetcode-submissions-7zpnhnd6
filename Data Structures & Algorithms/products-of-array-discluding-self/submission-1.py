class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro_list = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            pro_list.append(prod)
        return pro_list

        