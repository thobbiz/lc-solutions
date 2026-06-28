from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1

        for i in nums:
            prefix += i
            if (prefix - k) in seen:
                total += seen[prefix - k]
            seen[prefix] += 1

        return total
