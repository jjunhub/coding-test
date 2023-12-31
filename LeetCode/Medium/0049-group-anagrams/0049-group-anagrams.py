class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = collections.defaultdict(list)
        for str in strs:
            sortedStr = "".join(sorted(str))
            dct[sortedStr].append(str)
            
        return dct.values()