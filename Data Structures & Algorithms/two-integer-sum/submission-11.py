class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxdic = {}
        for i, n in enumerate(nums):
            idxdic[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in idxdic and idxdic[diff] != i:
                if idxdic[diff] < i:
                    return [idxdic[diff], i]
                return [i,idxdic[diff]]
        