from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        hashMap = {}
        result = 1

        hashMap[fruits[left]] = 1

        for right in range(1, len(fruits)):
            hashMap[fruits[right]] = hashMap.get(fruits[right], 0) + 1

            while len(hashMap) > 2:
                hashMap[fruits[left]] -= 1
                if hashMap[fruits[left]] == 0:
                    del hashMap[fruits[left]]
                left += 1

            result = max(result, right - left + 1)

        return result
