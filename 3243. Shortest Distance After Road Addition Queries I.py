class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj=[]
        for i in range(n):
            adj.append([i+1])        
        def sp():
            q=deque()
            q.append((0,0))
            visited=set()
            visited.add((0,0))
            while q:
                cur,ln=q.popleft()
                if cur==n-1:
                    return ln
                for nxt in adj[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt,ln+1))
        res=[]
        for first,last in queries:
            adj[first].append(last)
            res.append(sp())
        return res

