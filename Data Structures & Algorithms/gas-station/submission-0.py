class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)< sum(cost):
            return -1
        left = 0
        res = 0
        for i in range(len(gas)):
            left += gas[i] -cost[i]
            if left <0:
                left = 0
                res = i+1
        return res