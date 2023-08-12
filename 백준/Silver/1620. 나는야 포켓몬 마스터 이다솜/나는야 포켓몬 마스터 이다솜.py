import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nameDict = {}
numberDict = {}
for index in range(1, N+1):
    name = input().rstrip()
    nameDict[name] = index
    numberDict[index] = name

numbers = [str(i) for i in range(1,11)]

for _ in range(M):
    info = input().rstrip()
    if info[0] in numbers:
        print(numberDict[int(info)])
    else :
        print(nameDict[info])