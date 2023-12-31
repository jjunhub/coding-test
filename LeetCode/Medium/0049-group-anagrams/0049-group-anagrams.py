class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = collections.defaultdict(list)
        for idx, el in enumerate(strs):
            sortedStr = "".join(sorted(el))
            dct[sortedStr].append(idx)
            
        
        sortedDict = sorted(dct.items(), key = lambda x : len(x[1]))
        
    
        result = [ ]
        for el in sortedDict:
            tempResult = []
            for val in el[1]:
                tempResult.append(strs[val])
            result.append(tempResult)
            
        return result