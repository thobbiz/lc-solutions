from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def total_of_extremes(should_pop):
            stack = []
            total = 0

            for i in range(n + 1):
                while stack and (i == n or should_pop(nums[stack[-1]], nums[i])):
                    mid = stack.pop()
                    left = stack[-1] if stack else -1
                    total += nums[mid] * (mid - left) * (i - mid)
                stack.append(i)

            return total

        sum_of_maxes = total_of_extremes(lambda top, curr: top <= curr)
        sum_of_mins = total_of_extremes(lambda top, curr: top >= curr)

        return sum_of_maxes - sum_of_mins
