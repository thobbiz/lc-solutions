class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def dp(s1, s2):
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            n = len(s1)
            for i in range(1, n):
                # no swap
                if dp(s1[:i], s2[:i]) and dp(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                # swap
                if dp(s1[:i], s2[n - i :]) and dp(s1[i:], s2[: n - i]):
                    memo[(s1, s2)] = True
                    return True

            memo[(s1, s2)] = False
            return False

        return dp(s1, s2)
