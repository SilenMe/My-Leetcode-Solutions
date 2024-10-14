#we don't have maxHeap built in python so we will use min heap by converting the all the values in negative
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans=0
        minHeapArr=[-n for n in nums]
        heapq.heapify(minHeapArr)
        
        while k:
            n=-heapq.heappop(minHeapArr)
            ans+=n
            k-=1
            heapq.heappush(minHeapArr,-math.ceil(n/3))
        return ans

        
