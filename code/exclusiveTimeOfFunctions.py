from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            parts = log.split(":")
            fid = int(parts[0])
            typ = parts[1]
            timestamp = int(parts[2])

            if typ == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fid)
                prev_time = timestamp
            else:
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res