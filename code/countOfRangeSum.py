class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        def sort_count(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            count = sort_count(lo, mid) + sort_count(mid, hi)

            l = r = mid
            for i in range(lo, mid):
                while l < hi and prefix[l] - prefix[i] < lower:
                    l += 1
                while r < hi and prefix[r] - prefix[i] <= upper:
                    r += 1
                count += r - l

            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return sort_count(0, len(prefix))
