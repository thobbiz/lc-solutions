class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(2 * n - 1):
            if i % 2 == 0:
                l = r = i // 2
            else:
                l = i // 2
                r = i // 2 + 1

            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count
