from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numsMap = {}
        seen = set()
        res = []
        threshold = len(nums) // 3

        for n in nums:
            if n in seen:
                continue
            numsMap[n] = numsMap.get(n, 0) + 1
            if numsMap[n] > threshold:
                res.append(n)
                seen.add(n)

        return res
