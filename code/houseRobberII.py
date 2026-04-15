from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        prev2, prev1 = 0, 0
        for num in nums:
            current = max(prev2 + num, prev1)
            prev2, prev1 = prev1, current

        return prev1
