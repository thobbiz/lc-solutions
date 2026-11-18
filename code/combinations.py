class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(start):
            if len(path) == k:
                res.append(path[:])
                return

            needed = k - len(path)
            for i in range(start, n - needed + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res
