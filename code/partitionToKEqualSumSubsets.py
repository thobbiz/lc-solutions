class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(i: int) -> bool:
            if i == len(nums):
                return True

            seen = set()
            for j in range(k):
                if buckets[j] + nums[i] > target or buckets[j] in seen:
                    continue

                seen.add(buckets[j])
                buckets[j] += nums[i]
                if backtrack(i + 1):
                    return True
                buckets[j] -= nums[i]

            return False

        return backtrack(0)
