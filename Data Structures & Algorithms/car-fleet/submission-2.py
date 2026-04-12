class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        cars.sort(key = lambda x : x[0], reverse= True)
        stack =[]
        curtime = 0 
        for c in cars:
            time = (target-c[0]) / c[1]
            if time > curtime:
                stack.append(time)
                curtime = time
        return len(stack)
