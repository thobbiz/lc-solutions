import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if the list has only one character
        if len(strs) == 1:
            return [strs]

        # a map for storing anagrams and their correspoding strings in the list
        anagramMap = collections.defaultdict(list)

        # iterate through each string in the list
        for word in strs:
            # sort each string
            key = "".join(sorted(word))
            # add each string to the dictionary using the sorted string as a key
            anagramMap[key].append(word)

        return list(anagramMap.values())
