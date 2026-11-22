class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        n = len(s)

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == n:
                    res.append(".".join(parts))
                return

            remaining = n - start
            slots = 4 - len(parts)
            if remaining < slots or remaining > 3 * slots:
                return

            for length in range(1, 4):
                if start + length > n:
                    break

                seg = s[start:start + length]

                if len(seg) > 1 and seg[0] == "0":
                    break
                if int(seg) > 255:
                    break

                parts.append(seg)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])
        return res
