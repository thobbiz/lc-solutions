from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                threeSum = number + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([number, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
