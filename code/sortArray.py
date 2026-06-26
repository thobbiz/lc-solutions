from typing import List


class Solution:
    def merge(self, A, p, q, r):
        L = A[p : q + 1]
        R = A[q + 1 : r + 1]

        i, j, k = 0, 0, p
        lenL = len(L)
        lenR = len(R)

        while i < lenL and j < lenR:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < lenL:
            A[k] = L[i]
            i += 1
            k += 1

        while j < lenR:
            A[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, A, p, r):
        if p < r:
            q = (p + r) // 2
            self.mergeSort(A, p, q)
            self.mergeSort(A, q + 1, r)
            self.merge(A, p, q, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        p = 0
        r = len(nums) - 1
        self.mergeSort(nums, p, r)

        return nums
