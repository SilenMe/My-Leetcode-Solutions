class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.solNum=0
        def dfs(nums):
            if len(nums)==0:
                return [[]]
            main=[]
            initial=nums[0]
            remain=nums[1:]
            for item in dfs(remain):
                addItem=True
                addCombo=True
                if len(item)>1:
                    for i in range(len(item)-1):
                        if item[i+1]-item[i]==k:
                            addItem=False
                            break
                if len(item)>0:
                    for it in item:
                        if it-initial==k:
                            addCombo=False
                            break
                if addItem:
                    main.append(item)
                if addCombo:
                    self.solNum+=1
                    main.append([initial]+item)
            return main
        return len(dfs(nums))-1
