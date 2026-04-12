class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        cars.sort(key = lambda x : x[0], reverse= True)
        curtime = 0 
        fleet = 0
        for c in cars:
            time = (target-c[0]) / c[1]
            if time > curtime:
                fleet +=1
                curtime = time
        return fleet