import sys
input = sys.stdin.readline

N = int(input())

leftPtr = 1
rightPtr = 0
sum = 0
count = 0

while(rightPtr <= N) :
    if sum == N :
        count += 1
        rightPtr += 1
        sum += rightPtr
    elif sum < N :
        rightPtr += 1
        sum += rightPtr
    else :
        sum -= leftPtr
        leftPtr += 1

print(count)