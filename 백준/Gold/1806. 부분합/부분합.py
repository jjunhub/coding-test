import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

minLength = 100000 + 1 # 합이 S 이상을 만족하는 집합 중 최소 길이
totalSum = 0 # leftPtr부터 rightPtr까지의 합

totalSum += numbers[0]
leftPtr = 0
rightPtr = 0

while(rightPtr < N):
    if totalSum >= S : # S보다 크거나 같은 경우
        tempMinLength = rightPtr - leftPtr + 1
        if minLength > tempMinLength : # 최소 길이를 발견한 경우
            minLength = tempMinLength
        # 왼쪽 포인터를 이동시켜 값을 감소시킨다.
        totalSum -= numbers[leftPtr]
        leftPtr += 1
        if leftPtr > rightPtr :
            rightPtr = leftPtr

    else : # S보다 작은 경우
        rightPtr += 1
        if(rightPtr == N) : break
        totalSum += numbers[rightPtr]

print(minLength if minLength != 100000 + 1 else 0 )