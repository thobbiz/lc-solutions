from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(index, current_sum):
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            if index == len(nums):
                return 1 if current_sum == target else 0
            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]

        return dfs(0, 0)
