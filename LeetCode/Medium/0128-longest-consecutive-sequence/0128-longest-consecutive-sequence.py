class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _dict = {}
        for index, number in enumerate(nums):
            if number not in _dict :
                _dict[number] = index
        
        maxLength = 0
        length = 1
        
        for index, number in enumerate(nums):
            if number -1 not in _dict :
                while(True):    
                    if length > maxLength :
                        maxLength = length
                    if number + 1 in _dict: 
                        number +=1 
                        length += 1
                    else :
                        length = 1
                        break
            
        return maxLength