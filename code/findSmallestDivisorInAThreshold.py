from math import ceil
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(div):
            res = 0
            for i in nums:
                res += ceil(i / div)
            return res

        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if check(mid) <= threshold:
                high = mid
            else:
                low = mid + 1

        return low
