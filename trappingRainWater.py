import array
from typing import List


def trap(height: List[int]) -> int:
    left = 1
    right = len(height) - 2
    result = 0

    lMax = height[0]
    rMax = height[len(height) - 1]

    while left <= right:
        if rMax <= lMax:
            result += max(0, rMax - height[right])
            rMax = max(rMax, height[right])
            right -= 1
        else:
            result += max(0, lMax - height[left])
            lMax = max(lMax, height[left])
            left += 1

    return result


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    # Run the code
    result = trap(height)
    print(result)


if __name__ == "__main__":
    main()
