from typing import List


class Solution:
    def maxSubArrayNaive(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            currSum = 0

            for j in range(i, len(nums)):
                currSum = currSum + nums[j]

                res = max(res, currSum)

        return res

    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        maxEnding = nums[0]

        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            res = max(res, maxEnding)

        return res
