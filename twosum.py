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
        history[current] = index

    return result


def main():
    nums = [2, 7, 11, 15]
    target = 18

    # Run the code
    result = twoSum(nums, target)
    print(result)


if __name__ == "__main__":
    main()
