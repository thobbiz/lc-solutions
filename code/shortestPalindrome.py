class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        rev = s[::-1]
        combined = s + "#" + rev

        failure = [0] * len(combined)
        k = 0

        for i in range(1, len(combined)):
            while k > 0 and combined[i] != combined[k]:
                k = failure[k - 1]
            if combined[i] == combined[k]:
                k += 1
            failure[i] = k

        palin_len = failure[-1]
        remainder = s[palin_len:]

        return remainder[::-1] + s
