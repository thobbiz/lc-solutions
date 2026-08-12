from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                pre[i][j] = mat[i-1][j-1] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1]
        answer = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                r1, r2 = max(0, i - K), min(n - 1, i + K)
                c1, c2 = max(0, j - K), min(m - 1, j + K)
                answer[i][j] = pre[r2+1][c2+1] - pre[r1][c2+1] - pre[r2+1][c1] + pre[r1][c1]
        return answer
