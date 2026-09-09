class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        count = defaultdict(int)
        maxHeap = []
        res = []

        for n, f in zip(nums, freq):
            count[n] += f
            heapq.heappush(maxHeap, (-count[n], n))

            while maxHeap and -maxHeap[0][0] != count[maxHeap[0][1]]:
                heapq.heappop(maxHeap)

            res.append(-maxHeap[0][0] if maxHeap else 0)

        return res
