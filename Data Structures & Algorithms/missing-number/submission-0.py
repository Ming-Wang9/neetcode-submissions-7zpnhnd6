class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = set(nums)
        for i in range(n+1):
            if i not in new_nums:
                return i

