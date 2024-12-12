import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-i for i in gifts] #python only have minHeap so making elements negative to achieve maxHeap like functionality
        heapq.heapify(gifts)
        for _ in range(k):
            n=-heapq.heappop(gifts)
            heapq.heappush(gifts,-floor(sqrt(n)))
        return -sum(gifts)
