from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        hashMap = {}
        res = 0
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]
            hashMap[nums[r]] = hashMap.get(nums[r], 0) + 1
            while hashMap[nums[r]] > 1:
                hashMap[nums[l]] -= 1
                curr -= nums[l]
                l += 1
            res = max(res, curr)

        return res
