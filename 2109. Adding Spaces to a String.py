#should be easy
class Solution:
    def addSpaces(self,s:str,spaces:List[int])->str:
        start,arr=0,[]
        for end in spaces:
            arr.append(s[start:end])
            start=end        
        arr.append(s[start :])
        return " ".join(arr)
