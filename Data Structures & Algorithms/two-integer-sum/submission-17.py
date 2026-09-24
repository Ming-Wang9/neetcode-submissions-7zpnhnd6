class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        for i,n in enumerate(nums):
            numdict[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in numdict and numdict[diff] != i:
                return [i,numdict[diff]]
            
