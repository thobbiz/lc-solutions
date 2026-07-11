from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        hashMap = {0: 1}
        res = 0

        for r in range(len(nums)):
            prefix += nums[r]

            res += hashMap.get((prefix - goal), 0)

            hashMap[prefix] = hashMap.get(prefix, 0) + 1

        return res
