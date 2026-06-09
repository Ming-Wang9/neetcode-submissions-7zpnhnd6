class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inddict = {}
        for i,n in enumerate(nums):
            inddict[n] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in inddict and i != inddict[diff]:
                if i < inddict[diff]:
                    return [i,inddict[diff]]
                else:
                    return [inddict[diff], i]

        