class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()

        def dfs(city):
            seen.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in seen:
                    dfs(neighbor)
        res = 0
        for city in range(n):
            if city not in seen:
                dfs(city)
                res += 1


        return res
