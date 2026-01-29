def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """

    maxArea = 0
    leftPointer = 0
    rightPointer = len(height) - 1
    while leftPointer < rightPointer:
        maxArea = max(
            maxArea,
            (rightPointer - leftPointer)
            * min(height[leftPointer], height[rightPointer]),
        )
        if height[leftPointer] < height[rightPointer]:
            leftPointer += 1
        else:
            rightPointer -= 1
    return maxArea
