class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_map = {}
        for n in nums:
            num_map[n] = 1 + num_map.get(n, 0)
            if num_map[n] > 1:
                return n