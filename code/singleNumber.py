from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        for i in counts:
            if counts[i] == 1:
                return i
