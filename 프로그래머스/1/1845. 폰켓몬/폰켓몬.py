import collections
def solution(nums):
    answer = 0
    pocketmonDict = collections.defaultdict(int)
    for num in nums:
        pocketmonDict[num]+= 1
    
    
    answer = min( len(nums)//2, len(pocketmonDict.keys()))
    return answer