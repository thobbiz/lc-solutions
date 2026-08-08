from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = 0
        minPrefix = float('inf')

        for i in nums:
            curr += i
            minPrefix = min(minPrefix, curr)

        return max(1, 1 - minPrefix)
