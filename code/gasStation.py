from typing import List


class Solution:
    def canCompleteCircuitNaive(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        startIndex = -1

        for i in range(n):
            currGas = 0
            flag = True

            for j in range(n):
                index = (i + j) % n
                currGas += gas[index] - cost[index]

                if currGas < 0:
                    flag = False
                    break

            if flag:
                startIndex = i
                break

        return startIndex

    def canCompleteCircuitOptimal(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        startIndex = 0

        currGas = 0

        for i in range(n):
            currGas = currGas + gas[i] - cost[i]
            if currGas < 0:
                startIndex = i + 1
                currGas = 0

        currGas = 0
        for i in range(n):
            index = (i + startIndex) % n
            currGas = currGas + gas[index] - cost[index]
            if currGas < 0:
                return -1

        return startIndex
