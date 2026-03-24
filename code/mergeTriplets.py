from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target

        max_first, max_second, max_third = 0, 0, 0

        for first, second, third in triplets:
            if first <= x and second <= y and third <= z:
                max_first = max(first, max_first)
                max_second = max(second, max_second)
                max_third = max(third, max_third)

        return [max_first, max_second, max_third] == target
