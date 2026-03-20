from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = maxPos = last = 0

        for i in range(n):
            maxPos = max(maxPos, i + nums[i])

            if i == last:
                res += 1
                last = maxPos

        return res
