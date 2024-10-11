class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times=[(t[0],t[1],i) for i,t in enumerate(times)]
        times.sort()  #by default sorting will be done on first index

        uc=[]  #used chair (leaveTime,chair)
        ac=[i for i in range(len(times))]  #available chair

        for a,l,i in times:
            while uc and uc[0][0]<=a:
                _,chair=heapq.heappop(uc)
                heapq.heappush(ac,chair)
            chair=heapq.heappop(ac)
            heapq.heappush(uc,(l,chair))
            if i==targetFriend:
                return chair
        
