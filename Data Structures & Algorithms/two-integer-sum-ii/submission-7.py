class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idxrecord = {}
        
        for i, n in enumerate(numbers):
            idxrecord[n] = i
        
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in idxrecord and idxrecord[diff] != i:
                return [i + 1, idxrecord[diff] + 1]