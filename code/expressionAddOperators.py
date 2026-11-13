class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []
        n = len(num)

        def backtrack(i, path, value, prev):
            if i == n:
                if value == target:
                    res.append(path)
                return

            for j in range(i, n):
                if j > i and num[i] == "0":
                    break

                cur = int(num[i:j + 1])

                if i == 0:
                    backtrack(j + 1, str(cur), cur, cur)
                else:
                    backtrack(j + 1, path + "+" + str(cur), value + cur, cur)
                    backtrack(j + 1, path + "-" + str(cur), value - cur, -cur)
                    backtrack(j + 1, path + "*" + str(cur), value - prev + prev * cur, prev * cur)

        backtrack(0, "", 0, 0)
        return res
