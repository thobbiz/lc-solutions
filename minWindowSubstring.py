def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    targetMap = {}
    for char in t:
        targetMap[char] = targetMap.get(char, 0) + 1

    windowMap = {}
    formedCounter = 0
    required = len(targetMap)

    ans = float("inf"), 0, 0

    left = 0
    right = 0

    while right < len(s):
        char = s[right]
        windowMap[char] = windowMap.get(char, 0) + 1

        if char in targetMap and windowMap[char] == targetMap[char]:
            formedCounter += 1

        while left <= right and formedCounter == required:
            char_left = s[left]

            current_window_len = right - left + 1
            if current_window_len < ans[0]:
                ans = (current_window_len, left, right)

            windowMap[char_left] -= 1
            if char_left in targetMap and windowMap[char_left] < targetMap[char_left]:
                formedCounter -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


def main():
    s = "ADOBECODEBANC"
    t = "ABC"

    # Run the code
    result = minWindow(s, t)
    print(result)


if __name__ == "__main__":
    main()
