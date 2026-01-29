from collections import deque
from typing import List


def slidingWindowMax(nums: List[int], k: int) -> List[int]:
    result = []
    dq = deque()

    # initialize the queue with the first 3 elements
    for i in range(0, k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    for i in range(k, len(nums)):
        result.append(nums[dq[0]])

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        dq.append(i)

    result.append(nums[dq[0]])

    return result


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    # Run the code
    result = slidingWindowMax(nums, k)
    print(result)


if __name__ == "__main__":
    main()
