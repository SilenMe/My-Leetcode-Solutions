#https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=daily-question&envId=2024-02-28

#my first sol(not much optimised)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=[root]
        nextQueue=[]
        ini=root.val
        sol=[[0]]
        indi=[]
        
        while queue!=[] or nextQueue!=[]:
            if queue==[]:
                queue=nextQueue
                nextQueue=[]
                sol.append(indi)
                indi=[]
            if queue[0]:
                nextQueue.append(queue[0].left)
                nextQueue.append(queue[0].right)
            if queue[0]!=None:
                indi.append(queue[0].val)
             
            
            queue=queue[1:]
        return sol[-1][0]




# optimised solution(if we add rightChild first then add leftChild then the value of last node traversed will be the solution)
# my mistake was that I added left element first, in that case we have to keep track of levels and have to fetch the first value from the lastLevelValuesList
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q= deque([root])
        while q:
            node=q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return node.val
