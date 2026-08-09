from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        def helper(L: int, M: int) -> int:
            maxL = 0
            result = 0
            for i in range(L + M, n + 1):
                maxL = max(maxL, prefix[i - M] - prefix[i - M - L])
                result = max(result, maxL + prefix[i] - prefix[i - M])
            return result
        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))
