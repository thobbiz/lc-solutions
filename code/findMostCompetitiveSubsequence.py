from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, c in enumerate(nums):
            while stack and c < stack[-1] and ((n - i - 1) >= (k - len(stack))):
                stack.pop()
            if len(stack) < k:
                stack.append(c)

        return stack
