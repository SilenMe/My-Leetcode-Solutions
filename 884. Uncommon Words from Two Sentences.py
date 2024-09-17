class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count=defaultdict(int)
        ans=[]
        for item in s1.split(" ")+ s2.split(" "):
            count[item]+=1
        for item in count:
            if count[item]==1:
                ans.append(item)
        return ans
