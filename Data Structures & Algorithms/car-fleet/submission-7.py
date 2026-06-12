class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        for car in cars:
            stack.append((target-car[0])/car[1])
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)