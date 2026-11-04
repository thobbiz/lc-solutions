class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        points = [0] * (max(nums) + 1)
        for n in nums:
            points[n] += n

        take, skip = 0, 0
        for p in points:
            take, skip = skip + p, max(take, skip)

        return max(take, skip)
