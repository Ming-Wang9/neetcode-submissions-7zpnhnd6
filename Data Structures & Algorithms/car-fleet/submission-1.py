class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        cars.sort(key=lambda x : x[0], reverse = True)
        fleet, curtime = 0, 0
        for p,s in cars:
            time = (target -p) /s
            if time > curtime:
                fleet += 1
                curtime = time
        return fleet 