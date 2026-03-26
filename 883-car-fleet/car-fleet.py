class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  
        fleets = 0
        lead_time = 0.0
        for pos, sp in cars:
            time = (target - pos) / sp
            if time > lead_time:
                fleets += 1
                lead_time = time
        return fleets
