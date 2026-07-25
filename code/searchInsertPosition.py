from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high, low = len(nums) - 1, 0

        while high >= low:
            mid = (high + low) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                low = mid + 1

        return low
