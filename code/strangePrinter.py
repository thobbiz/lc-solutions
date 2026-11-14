class Solution:
    def strangePrinter(self, s: str) -> int:
        chars = []
        for c in s:
            if not chars or chars[-1] != c:
                chars.append(c)

        n = len(chars)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j] + 1
                for k in range(i + 1, j + 1):
                    if chars[k] == chars[i]:
                        gap = dp[i + 1][k - 1] if k - 1 >= i + 1 else 0
                        dp[i][j] = min(dp[i][j], gap + dp[k][j])

        return dp[0][n - 1]
