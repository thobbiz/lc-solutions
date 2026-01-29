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


def main():
    s = "ABAB"
    k = 2

    # Run the code
    result = characterReplacement(s, k)
    print(result)


if __name__ == "__main__":
    main()
