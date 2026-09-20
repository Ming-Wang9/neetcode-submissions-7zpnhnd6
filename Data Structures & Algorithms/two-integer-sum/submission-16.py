class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #assuming there is no duplication
        indexmap = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in indexmap:
                return [indexmap[diff], i]
            indexmap[n] = i