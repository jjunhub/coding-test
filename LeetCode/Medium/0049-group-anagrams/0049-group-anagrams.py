class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for idx, el in enumerate(strs):
            sortedStr = "".join(sorted(el))
            
            if sortedStr in dct:
                dct[sortedStr].append(idx)
            else :
                dct[sortedStr] = [idx]
        
        sortedDict = sorted(dct.items(), key = lambda x : len(x[1]))
        
    
        result = [ ]
        for el in sortedDict:
            tempResult = []
            for val in el[1]:
                tempResult.append(strs[val])
            result.append(tempResult)
            
        return result