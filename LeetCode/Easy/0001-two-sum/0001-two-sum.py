class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        results = []
        for number in nums:
            if number in _dict :
                _dict[number] += 1
            else :
                _dict[number] = 1
        
        for index, number in enumerate(nums):
            if target - number in _dict:
                if target == number * 2 :
                    if _dict[number] >= 2 :
                        results.append(index)
                else :
                    results.append(index)
                    
        return results