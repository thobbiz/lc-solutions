from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1

        while even < len(nums):
            if nums[even] % 2 == 0:
                even += 2
            else:
                while nums[odd] % 2 != 0:
                    odd += 2
                nums[even], nums[odd] = nums[odd], nums[even]

        return nums
