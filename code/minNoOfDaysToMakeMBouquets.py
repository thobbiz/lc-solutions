from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def bouquetsByDay(day):
            bouquets, streak = 0, 0
            for bloom in bloomDay:
                if bloom <= day:
                    streak += 1
                    if streak == k:
                        bouquets += 1
                        streak = 0
                else:
                    streak = 0
            return bouquets
        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if bouquetsByDay(mid) >= m:
                hi = mid
            else:
                lo = mid + 1
        return lo
