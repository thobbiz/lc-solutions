from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        dp = [1] * n
        pointers = [0] * k
        next_vals = primes[:]

        for i in range(1, n):
            min_val = min(next_vals)
            dp[i] = min_val

            for j in range(k):
                if next_vals[j] == min_val:
                    pointers[j] += 1
                    next_vals[j] = primes[j] * dp[pointers[j]]

        return dp[n - 1]
