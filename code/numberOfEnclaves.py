class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        stack = []

        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and grid[r][c] == 1:
                    grid[r][c] = 0
                    stack.append((r, c))

        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    stack.append((nr, nc))

        return sum(sum(row) for row in grid)
