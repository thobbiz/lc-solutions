from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            rightSum = total - leftSum - num
            if leftSum == rightSum:
                return i
            leftSum += num
        return -1
