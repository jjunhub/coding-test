from heapq import heappush, heappop
from collections import defaultdict
def solution(operations):
    maxH = []
    minH = []
    dict = defaultdict(int)
    
    def insertNum(index, num):
        heappush(maxH, ((-1) * num, index))
        heappush(minH, (num, index))
        dict[index] = num
    
    def removeMax():
        if not maxH :
            return 
        
        _, index = heappop(maxH)
        if dict[index] != 0 :
            # 한 번도 지워지지 않은 값이라면, 0으로 만들어 지운다.
            del dict[index]
        else :
            # 이미 지워진 값이었다면,
            while maxH and dict[index] == 0:
                # 다음 큰 값을 뽑아서, 지워지지 않은 값일 때까지 뽑는다.
                _, index = heappop(maxH)
            del dict[index]
        
    def removeMin():
        if not minH :
            return
        
        _, index = heappop(minH)
        if dict[index] != 0 :
            del dict[index]
        else :
            while minH and dict[index] == 0:
                _, index = heappop(minH)
            del dict[index]
                 
    for index, oper in enumerate(operations):
        command, num = oper.split()
        # print(f'command = {command}, num = {num}')
        if command == "I":
            insertNum(index, int(num))
        elif num == "-1" : # D 1
            removeMin()
        else : # D 1
            removeMax()
        # print(f'maxH = {maxH}, minH = {minH}')
    
    if not dict:
        return [0, 0]
    else :
        return [ max(dict.values()), min(dict.values())]