class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numshash = {}
        for num in nums:
            if num not in numshash:
                numshash[num] = 0
            numshash[num] += 1

        countlist = sorted(numshash.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in countlist[:k]]

            