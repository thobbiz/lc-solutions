class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        res = 0
        stack = []
        for i, c in enumerate(nums):
            if stack and c >= nums[stack[-1]]:
                continue
            stack.append(i)
        print(stack)

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                res = max(res, i - stack[-1])
                stack.pop()

        return res
