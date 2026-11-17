class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = []
        path = list(s)

        def backtrack(i: int) -> None:
            if i == len(s):
                res.append("".join(path))
                return

            if s[i].isalpha():
                path[i] = s[i].lower()
                backtrack(i + 1)
                path[i] = s[i].upper()
                backtrack(i + 1)
            else:
                backtrack(i + 1)

        backtrack(0)
        return res
