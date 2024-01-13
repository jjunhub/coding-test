import collections
def solution(clothes):
    answer = 1
    _dict = collections.defaultdict(int)
    
    for _, clothType in clothes:
        _dict[clothType] += 1
        
    for val in _dict.values():
        answer *=  (val + 1)
        
    return answer - 1