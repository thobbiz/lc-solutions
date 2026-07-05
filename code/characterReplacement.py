def characterReplacement(s: str, k: int) -> int:
    cnt = {}
    l = 0
    max_freq = 0
    res = 0

    for r, c in enumerate(s):
        cnt[c] = cnt.get(c, 0) + 1
        max_freq = max(max_freq, cnt[c])

        # check for window validity
        window_size = r - l + 1
        replace_char = window_size - max_freq

        # shrink window when invalid
        if replace_char > k:
            cnt[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res


def charReplacement(s: str, k: int) -> int:
    count = {}
    left = 0
    maxFreq = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        maxFreq = max(maxFreq, count[s[right]])
        if (right - left + 1) - maxFreq > k:
            count[s[left]] -= 1
            left += 1

        print(f"C[{s[right]}] = {count[s[right]]}")
        print(f"maxFreq = {maxFreq}")
        print(f"right = {right}")
        print(f"left = {left} \n\n")

    return len(s) - left


def main():
    s = "AABABBA"
    k = 1

    # Run the code
    result = charReplacement(s, k)
    print(result)


if __name__ == "__main__":
    main()
