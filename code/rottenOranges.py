from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfsQueue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    bfsQueue.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while bfsQueue and fresh > 0:
            for i in range(len(bfsQueue)):
                r, c = bfsQueue.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (
                        row < 0
                        or row == ROWS
                        or col < 0
                        or col == COLS
                        or grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2
                    bfsQueue.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
