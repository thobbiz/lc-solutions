class Solution:
    def grayCode(self, n: int) -> list[int]:
        res, seen = [0], {0}

        def dfs(cur):
            if len(res) == 1 << n:
                return True
            for b in range(n):
                nxt = cur ^ (1 << b)
                if nxt not in seen:
                    seen.add(nxt); res.append(nxt)
                    if dfs(nxt):
                        return True
                    res.pop(); seen.remove(nxt)
            return True

        dfs(0)
        return res
