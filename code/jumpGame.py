from typing import List


class Solution:
    def minJumps(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] == 0:
            return -1

        maxReach = 0
        currReach = 0
        jump = 0

        for i in range(n):
            maxReach = max(maxReach, i + nums[i])

            if maxReach >= n - 1:
                return jump + 1

            if i == currReach:
                if i == maxReach:
                    return -1
                else:
                    jump += 1
                    currReach = maxReach

        return -1

    def canJump(self, nums: List[int]) -> bool:
        ans = self.minJumps(nums)

        if ans == -1:
            return False

        return True
