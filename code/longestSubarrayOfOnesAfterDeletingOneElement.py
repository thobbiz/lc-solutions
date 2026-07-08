from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        result = 0
        xero_nums = 0

        if 0 not in nums:
            return len(nums) - 1

        for right in range(len(nums)):
            if nums[right] == 0:
                xero_nums += 1
            while xero_nums > 1:
                if nums[left] == 0:
                    xero_nums -= 1
                left += 1
            result = max(result, right - left + 1)

        return result - 1
