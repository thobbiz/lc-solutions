from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = 0
        even = 1
        odd = 0
        res = 0

        for e in arr:
            prefix += e
            if prefix % 2 != 0:
                res += even
                odd += 1
            else:
                res += odd
                even += 1

        return res % (10**9 + 7)
