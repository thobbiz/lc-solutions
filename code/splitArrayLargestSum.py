from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def subarraysNeeded(cap):
            subarrays, currentSum = 1, 0
            for num in nums:
                if currentSum + num > cap:
                    subarrays += 1
                    currentSum = num
                else:
                    currentSum += num
            return subarrays
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if subarraysNeeded(mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
