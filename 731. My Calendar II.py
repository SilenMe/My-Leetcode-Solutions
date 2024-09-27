class MyCalendarTwo:
    def __init__(self):
        self.no=[]
        self.o=[]
    def book(self, start: int, end: int) -> bool:
        for s,e in self.o:
            if not(end<=s or e<=start):
                return False
        for s,e in self.no:
            if not(end<=s or e<=start):
                self.o.append((max(s,start),min(e,end)))
        self.no.append((start,end))
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
