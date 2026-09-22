class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0

        for b, u in boxTypes:
            if truckSize <= 0:
                break
            take = min(b, truckSize)
            res += take * u
            truckSize -= take
        return res
