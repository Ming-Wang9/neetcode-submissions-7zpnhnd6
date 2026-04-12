class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p,s in zip(position, speed)]
        cars.sort(key=lambda x : x[0], reverse = True)
        stack = []
        for c in cars:
            stack.append((target-c[0])/c[1])
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
