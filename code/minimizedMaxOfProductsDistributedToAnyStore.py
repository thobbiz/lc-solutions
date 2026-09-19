from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        high, low = max(quantities), 1

        while low < high:
            mid = (low + high) // 2

            curr = 0
            for q in quantities:
                curr += ceil(q/mid)

            if curr <= n:
                high = mid
            else:
                low = mid + 1

        return low
