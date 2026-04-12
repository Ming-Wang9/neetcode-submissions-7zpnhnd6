class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap= {}
        for i in range(len(nums)):
            nummap[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nummap and nummap[diff] != i:
                return [i,nummap[diff]]
        return []