class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)        
        fleets = 0
        cur_time = 0 
        for p, s in cars:
            time = (target - p) / s
            if time > cur_time:   
                fleets += 1
                cur_time = time   
        return fleets