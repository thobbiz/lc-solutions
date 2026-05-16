from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = [-1] * n

        cols = set()
        diag = set()
        anti_diag = set()

        def backtrack(row):
            if row == n:
                solution = []
                for r in range(n):
                    solution.append("." * board[r] + "Q" + "." * (n - board[r] - 1))
                results.append(solution)
                return

            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti_diag:
                    continue

                board[row] = col
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)

        backtrack(0)
        return results
