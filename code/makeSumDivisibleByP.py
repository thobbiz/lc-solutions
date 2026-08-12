from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        seen = {0: -1}
        curr = 0
        res = len(nums)
        for i, num in enumerate(nums):
            curr = (curr + num) % p
            complement = (curr - target + p) % p
            if complement in seen:
                res = min(res, i - seen[complement])
            seen[curr] = i
        return res if res < len(nums) else -1
