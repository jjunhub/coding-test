class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _dict = {}
        for number in nums:
            if number not in _dict :
                _dict[number] = True
                
        maxLength = 0
        
        for number in nums:
            if number -1 not in _dict :
                cnt = 1
                target = number + 1
                while target in _dict:
                    target += 1
                    cnt += 1
                maxLength = max(maxLength, cnt)
                
        return maxLength