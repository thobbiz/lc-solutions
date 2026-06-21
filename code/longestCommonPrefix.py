from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]

    prefix = ""
    m = len(strs[1])
    for i in range(len(strs[0])):
        if i == m:
            break
        if strs[0][i] == strs[1][i]:
            prefix += strs[1][i]
        else:
            break

    for i in range(2, len(strs)):
        count = 0
        for j in range(min(len(prefix), len(strs[i]))):
            if prefix[j] == strs[i][j]:
                count += 1
            else:
                break
        if count == 0:
            return ""
        else:
            prefix = prefix[0:count]

    return prefix


def main():
    input = ["flower", "flow", "flight"]
    print(longestCommonPrefix(input))


if __name__ == "__main__":
    main()
