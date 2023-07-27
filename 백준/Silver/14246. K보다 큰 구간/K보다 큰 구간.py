import sys
input = sys.stdin.readline

n = int(input())
_list = list(map(int, input().split()))
target = int(input())

ptrR = ptrL = result = 0
tempSum = _list[0]

while True:
    if tempSum > target:
        result += len(_list)-ptrR
        tempSum -= _list[ptrL]
        ptrL += 1
    else : # tempSum <= target:
        ptrR += 1
        if(ptrR == len(_list)) : break
        tempSum += _list[ptrR]
    
print(result)