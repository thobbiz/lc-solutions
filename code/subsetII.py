from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        t = []

        def backtrack(i: int):
            if i == len(nums):
                res.append(t[:])
                return
            t.append(nums[i])
            backtrack(i + 1)

            x = t.pop()
            while (i + 1) < len(nums) and nums[i + 1] == x:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res
