class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def solve(expr: str) -> list[int]:
            if expr in memo:
                return memo[expr]

            results = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1 :])

                    for l in left:
                        for r in right:
                            if ch == "+":
                                results.append(l + r)
                            elif ch == "-":
                                results.append(l - r)
                            else:
                                results.append(l * r)

            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return solve(expression)
