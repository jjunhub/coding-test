class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = collections.defaultdict(list)
        for idx, el in enumerate(strs):
            sortedStr = "".join(sorted(el))
            dct[sortedStr].append(idx)
            
        result = [ ]
        for key, values in dct.items():
            tempResult = []
            for val in values:
                tempResult.append(strs[val])
            result.append(tempResult)
            
        return result