from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        if sorted(nums) == nums:
            return 0

        stack = []
        res = 0
        for n in nums:
            steps = 0
            while stack and n >= stack[-1][0]:
                steps = max(steps, stack.pop()[1])
            if stack:
                steps += 1
                res = max(res, steps)
            stack.append((n, steps))
        return res
