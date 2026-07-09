class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        l = 0
        result = 0
        curr = 0

        for r in range(len(s)):
            if (r - l + 1) > k:
                if s[l] in vowels:
                    curr -= 1
                l += 1

            if s[r] in vowels:
                curr += 1

            result = max(result, curr)

        return result
