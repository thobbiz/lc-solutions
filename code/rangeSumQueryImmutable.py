from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.addUp = []

        prev = 0
        for n in nums:
            self.addUp.append(prev + n)
            prev = prev + n

    def sumRange(self, left: int, right: int) -> int:
        prev = 0
        if left > 0:
            prev = self.addUp[left - 1]

        return self.addUp[right] - prev


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
