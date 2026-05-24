class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n
        res = 0

        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif dp[i - 1] > 0:
                    j = i - dp[i - 1] - 1
                    if j >= 0 and s[j] == "(":
                        dp[i] = dp[i - 1] + 2
                        if j - 1 >= 0:
                            dp[i] += dp[j - 1]
                res = max(res, dp[i])

        return res
