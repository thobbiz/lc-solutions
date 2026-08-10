from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.array = [0] * self.n
        self.tree = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self.update(i, num)

    def _add(self, index: int, delta: int) -> None:
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def _prefix_sum(self, index: int) -> int:
        i = index + 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.array[index]
        self._add(index, delta)
        self.array[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right) - self._prefix_sum(left - 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
