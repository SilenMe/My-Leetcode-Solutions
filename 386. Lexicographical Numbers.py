#wrong solution when you only consider leetcode default testcases
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        master=[[] for _ in range(9)]
        for i in range(1,n+1):
            s=str(i)
            num=int(s[0])-1
            master[num].append(i)

        sol=[]
        for item in master:
            sol+=item
        return sol

#backtracking solution
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        def dfs(cur):
            if cur>n:
                return
            res.append(cur)
            cur *=10
            for i in range(10):
                dfs(cur+i)
        for i in range(1,10):
            dfs(i)
        return res
