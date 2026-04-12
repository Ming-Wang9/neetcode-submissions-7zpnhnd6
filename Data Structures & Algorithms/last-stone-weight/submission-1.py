class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >1:
            fst = stones.pop()
            scd = stones.pop()
            if fst!=scd:
                stones.append(fst-scd)
                stones.sort()
        return stones[0] if stones else 0