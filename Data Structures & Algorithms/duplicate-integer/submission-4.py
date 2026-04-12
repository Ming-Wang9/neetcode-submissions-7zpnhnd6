class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for n in nums:
        #     if n in seen:
        #         return True
        #     seen.add(n)
        # return False
        numset = set(nums)
        if len(numset) != len(nums):
            return True
        return False