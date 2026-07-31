from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            d, cur = 1, 0
            for w in weights:
                if cur + w > capacity:
                    d += 1
                    cur = 0
                cur += wfet
            return d <= days
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if canShip(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
