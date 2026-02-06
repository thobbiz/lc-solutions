from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        history = set()
        n = len(nums) - 1

        for num in nums:
            if num in history:
                return num
            history.add(num)
        return 0
