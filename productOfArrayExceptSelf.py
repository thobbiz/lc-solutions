from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create the result array(length of the nums array)
        result = [1] * (len(nums))

        # calculate the product of everything to the LEFT of index i(prefix)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # calculate the product of everything to the RIGHT of index i(postfix)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
