from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, cur, remaining):
            if remaining == 0:
                result.append(cur.copy())
                return

            for j in range(i, len(candidates)):
                if candidates[j] > remaining:
                    break
                cur.append(candidates[j])
                dfs(j, cur, remaining - candidates[j])
                cur.pop()

        dfs(0, [], target)
        return result
