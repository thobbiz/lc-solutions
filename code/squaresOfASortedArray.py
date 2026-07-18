from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pos = len(nums) - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[pos] = nums[l] ** 2
                l += 1
            else:
                result[pos] = nums[r] ** 2
                r -= 1

            pos -= 1

        return result
