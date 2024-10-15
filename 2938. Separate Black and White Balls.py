class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        swap=0
        for item in s:
            if item == '1':
                swap += 1
            else:
                ans += swap
        return ans     
        
