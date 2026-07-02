from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        hashMap = {}
        result = 0

        for i in nums1:
            for j in nums2:
                hashMap[i + j] = hashMap.get((i + j), 0) + 1

        for i in nums3:
            for j in nums4:
                if -(i + j) in hashMap:
                    result += hashMap[-(i + j)]

        return result
