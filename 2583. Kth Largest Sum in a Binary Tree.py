# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue=[root]
        sL=[]
        queueNext=[]              #to store the next level element
        s=0
        while queue:
            popped=queue.pop()
            s+=popped.val
            if popped.left!=None:
                queueNext.append(popped.left)
            if popped.right!=None:
                queueNext.append(popped.right)
            if queue==[]:           
                queue=queueNext        #if cur level is done, now use next level queue
                queueNext=[]
                sL.append(s)
                s=0            
        sL.sort()
        if len(sL)<k:
            return -1
        return sL[-k]
        
        
