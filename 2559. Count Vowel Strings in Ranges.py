class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={'a':0,'e':0,'i':0,'o':0,'u':0} # hashtable>set>string>arr
        prefixSum=0
        arr=[0 for _ in range(len(words)+1)]
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefixSum+=1
            arr[i+1]=prefixSum
        for i in range(len(queries)):
            queries[i]=arr[queries[i][1]+1]-arr[queries[i][0]]
        return queries
