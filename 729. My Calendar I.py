#brute force
class MyCalendar:
    def __init__(self):
        self.vals=[[]]
    def book(self, start: int, end: int) -> bool:
        for items in self.vals:            
            if items!=[]:
                if max(start, items[0]) < min(end, items[1]):
                    return False
        self.vals.append([start,end])
        #print(self.vals)
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



#after hint: optimizing it using binary tree with two values in node.
class Tree:
    def __init__(self,start,end):
        self.left=None
        self.right=None
        self.start=start
        self.end=end
    def insert(self,start,end):
        curr=self
        while True:
            if start>=curr.end:
                if not curr.right:
                    curr.right=Tree(start,end)
                    return True
                curr=curr.right
            elif end<=curr.start:
                if not curr.left:
                    curr.left=Tree(start,end)
                    return True
                curr=curr.left
            else:
                return False

class MyCalendar:

    def __init__(self):
        self.root=None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root=Tree(start,end)
            return True
        return self.root.insert(start,end)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
