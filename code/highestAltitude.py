from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0
        res = 0

        for i in gain:
            prev += i
            res = max(res, prev)

        return res
