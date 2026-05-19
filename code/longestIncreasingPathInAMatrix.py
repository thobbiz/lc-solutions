from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}  # (r, c) -> longest increasing path

        def dfs(r, c, prev_val):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            if matrix[r][c] <= prev_val:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            cache[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -float("inf"))

        return max(cache.values())
