import math
from typing import List


class Solution:
    def build(self, edges: List[List[int]], root: int = 1):
        self.n = len(edges) + 1
        self.m = int(math.log2(self.n)) + 2
        self.e = [[] for _ in range(self.n + 1)]
        self.d = [0] * (self.n + 1)
        self.f = [[0] * self.m for _ in range(self.n + 1)]
        for u, v in edges:
            self.e[u].append(v)
            self.e[v].append(u)
        self.dfs(root)
        for i in range(1, self.m):
            for x in range(1, self.n + 1):
                self.f[x][i] = self.f[self.f[x][i - 1]][i - 1]

    def dfs(self, root: int):
        stack = [(root, 0)]
        while stack:
            x, pa = stack.pop()
            self.f[x][0] = pa
            for y in self.e[x]:
                if y == pa:
                    continue
                self.d[y] = self.d[x] + 1
                stack.append((y, x))

    def get_lca(self, u: int, v: int) -> int:
        if self.d[u] < self.d[v]:
            u, v = v, u
        for i in range(self.m - 1, -1, -1):
            if self.d[self.f[u][i]] >= self.d[v]:
                u = self.f[u][i]
        if u == v:
            return u
        for i in range(self.m - 1, -1, -1):
            if self.f[u][i] != self.f[v][i]:
                u = self.f[u][i]
                v = self.f[v][i]
        return self.f[u][0]

    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        self.build(edges)
        MOD = 10**9 + 7
        ans = []
        for u, v in queries:
            lca = self.get_lca(u, v)
            k = self.d[u] + self.d[v] - 2 * self.d[lca]
            ans.append(0 if k == 0 else pow(2, k - 1, MOD))
        return ans
