from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, openInt, closeInt):
            if len(curr) == 2 * n:
                return res.append(curr)
            if openInt < n:
                backtrack(curr + "(", openInt + 1, closeInt)
            if closeInt < openInt:
                backtrack(curr + ")", openInt, closeInt + 1)

        backtrack("", 0, 0)
        return res
