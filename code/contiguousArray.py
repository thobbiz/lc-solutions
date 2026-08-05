from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        index_map = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in index_map:
                max_length = max(max_length, i - index_map[count])
            else:
                index_map[count] = i
        return max_length
