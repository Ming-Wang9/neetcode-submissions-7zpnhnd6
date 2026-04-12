class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numset = set()
        for n in nums:
            if n not in numset:
                numset.add(n)
            else:
                return n