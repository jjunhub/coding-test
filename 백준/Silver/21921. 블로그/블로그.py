import sys
input = sys.stdin.readline

N, X = map(int, input().split())
# N일만큼 입력, X일 누적합 구하기

visitor = list(map(int, input().split()))
maxVisitor = sum(visitor[0:X]) # 최대 방문자 수
maxCount = 0 # 최대 방문자 수를 기록한 횟수
totalSum = 0 # X일간의 방문자 수

leftPtr = 0
rightPtr = X-1
totalSum += maxVisitor # 첫번째 합계 더해놓기

while(True):
    if(maxVisitor == totalSum):
        maxCount += 1
    elif(maxVisitor < totalSum):
        maxVisitor = totalSum
        maxCount = 1
        
    if(rightPtr == N-1) : break
    totalSum = totalSum - visitor[leftPtr] + visitor[rightPtr+1]
    leftPtr += 1
    rightPtr += 1

if maxVisitor == 0:
    print("SAD")
else :
    print(maxVisitor)
    print(maxCount)