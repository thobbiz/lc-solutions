from typing import List


def minEatingSpeed(self, piles: List[int], h: int) -> int:
    low, high = 1, max(piles)

    result = high

    while low <= high:
        mid = (low + high) // 2
        if self.can_finish(mid, piles, h):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


def can_finish(self, speed: int, piles: list[int], h: int) -> bool:
    total_hours = 0
    for pile in piles:
        total_hours += (pile + speed - 1) // speed

        if total_hours > h:
            return False

    return total_hours <= h
