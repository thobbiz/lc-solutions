from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k: int) -> int:
            if k < 0:
                return 0
            left = 0
            curr = 0
            result = 0

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    curr += 1

                while curr > k:
                    if nums[left] % 2 != 0:
                        curr -= 1
                    left += 1

                result += right - left + 1

            return result

        return atMost(k) - atMost(k - 1)
