from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))

        cars.sort(key=lambda x: x[0], reverse=True)

        fleets = 0
        last_fleet_time = 0.0

        for _, time in cars:
            if time > last_fleet_time:
                fleets += 1
                last_fleet_time = time

        return fleets
