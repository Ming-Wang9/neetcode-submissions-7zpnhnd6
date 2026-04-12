class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for n in nums:
            if n-1 not in numset:
                length = 1
                while n+length in numset:
                    length+=1
                maxlen = max(maxlen, length)
        return maxlen