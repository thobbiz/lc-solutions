def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []

    # for lookup
    history = {}

    for index, current in enumerate(nums):
        value = target - current
        if value in history:
            result.append(index)
            result.append(history[value])
            break

    return result
