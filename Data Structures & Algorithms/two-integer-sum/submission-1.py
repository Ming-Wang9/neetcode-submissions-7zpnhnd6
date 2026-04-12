class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashnums ={}
        index1 = 0
        index2 = 0
        for i in range (len(nums)):
            hashnums[nums[i]] = i
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in hashnums and hashnums[diff] != i:
                index1 = i
                index2 = int(hashnums[diff])
                return [index1, index2]
        return [index1, index2]
        