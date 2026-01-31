from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums)
    pivot = findPivot(nums)

    if nums[pivot] == target:
        return pivot

    if pivot == 0:
        return binSearch(nums, target, 0, n - 1)

    if nums[0] <= target:
        return binSearch(nums, target, 0, pivot - 1)
    return binSearch(nums, target, pivot + 1, n - 1)


def findPivot(nums: List[int]) -> int:
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (high + low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return low


def binSearch(nums: List[int], target: int, low: int, high: int) -> int:
    while high >= low:
        mid = (high + low) // 2
        if target < nums[mid]:
            high = mid - 1
        elif target == nums[mid]:
            return mid
        else:
            low = mid + 1
    return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3

    # Run the code
    result = search(nums, target)
    print(result)


if __name__ == "__main__":
    main()
