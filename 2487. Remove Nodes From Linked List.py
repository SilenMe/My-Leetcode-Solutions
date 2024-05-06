class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        stk=[]
        for v in nums:
            while stk and stk[-1]<v:
                stk.pop()
            stk.append(v)
        dummy=ListNode()
        head=dummy
        for item in stk:
            head.next=ListNode(item)
            head=head.next
        return dummy.next



class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head.next=self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next 
        else:
            return head
