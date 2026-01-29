from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        n = 0

        while n <= row:
            if n == row:
                return binSearch(matrix[n], target)
            elif target > matrix[n][col]:
                n += 1
            else:
                if binSearch(matrix[n], target):
                    return True
                else:
                    n += 1


def binSearch(nums: List[int], target: int) -> bool:
    low = 0
    high = len(nums) - 1

    while high >= low:
        mid = (high + low) // 2
        if target < nums[mid]:
            high = mid - 1
        elif target == nums[mid]:
            return True
        else:
            low = mid + 1
    return False
