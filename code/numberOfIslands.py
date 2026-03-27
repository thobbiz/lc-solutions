from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isSafe(grid, r, c, visited):
            n = len(grid)
            m = len(grid[0])
            return 0 <= r < n and 0 <= c < m and grid[r][c] == "1" and not visited[r][c]

        def bfs(grid, visited, startR, startC):
            dRow = [-1, 1, 0, 0]
            dCol = [0, 0, -1, 1]
            q = deque()
            q.append((startR, startC))
            visited[startR][startC] = True
            while q:
                r, c = q.popleft()
                for k in range(4):
                    newR = r + dRow[k]
                    newC = c + dCol[k]
                    if isSafe(grid, newR, newC, visited):
                        visited[newR][newC] = True
                        q.append((newR, newC))

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        islandCount = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(grid, visited, r, c)
                    islandCount += 1

        return islandCount
