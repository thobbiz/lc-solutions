from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def backtrack(curr: int):
            if len(str(curr)) == n:
                if curr != None:
                    res.append(curr)
                return

            if k == 0:
                backtrack(( curr * 10) + (curr%10) )
            else:
                if (curr%10) + k < 10:
                    backtrack(( curr * 10) + ((curr%10) + k) )

                if (curr%10) - k > -1:
                    backtrack(( curr * 10) + ((curr%10) - k) )

        for i in range(1, 10):
            curr = i
            backtrack(curr)

        return res
