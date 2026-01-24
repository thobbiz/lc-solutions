def checkInclusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)

    if n1 > n2:
        return False

    s1_count = [0] * 26
    s2_count = [0] * 26

    for i in range(n1):
        s1_count[ord(s1[i]) - ord("a")] += 1
        s2_count[ord(s2[i]) - ord("a")] += 1

    if s1_count == s2_count:
        return True

    for i in range(n1, n2):
        s2_count[ord(s2[i]) - ord("a")] += 1
        s2_count[ord(s2[i - n1]) - ord("a")] -= 1

        if s1_count == s2_count:
            return True

    return False


def main():
    s1 = "a"
    s2 = "eidbaooo"

    # Run the code
    result = checkInclusion(s1, s2)
    print(result)

    s1 = "ab"
    s2 = "eidboaoo"

    # Run the code
    result = checkInclusion(s1, s2)
    print(result)

    s1 = "a"
    s2 = "ab"

    result = checkInclusion(s1, s2)
    print(result)


if __name__ == "__main__":
    main()
