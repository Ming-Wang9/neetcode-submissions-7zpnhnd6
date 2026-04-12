class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap= {}
        for i in range(len(nums)):
            nummap[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return [i,nummap[diff]]
        