class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def sort(lo, hi):
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)

            j = mid
            for i in range(lo, mid):
                while j < hi and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid

            merged = []
            l, r = lo, mid
            while l < mid and r < hi:
                if nums[l] <= nums[r]:
                    merged.append(nums[l])
                    l += 1
                else:
                    merged.append(nums[r])
                    r += 1
            merged.extend(nums[l:mid])
            merged.extend(nums[r:hi])
            nums[lo:hi] = merged

            return count

        return sort(0, len(nums))
