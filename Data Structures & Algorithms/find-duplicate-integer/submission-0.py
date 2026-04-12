class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count ={}
        for num in nums:
            count[num] = count.get(num,0)+1
            if count[num] > 1:
                return num
