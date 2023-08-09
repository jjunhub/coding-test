import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dolls = list(map(int, input().split()))

leftPtr = 0
rightPtr = 0
count = 0
minLength = N

if dolls[rightPtr] == 1:
    count += 1

while(rightPtr < N):
    if count >= K :
        minLength = min(minLength, rightPtr - leftPtr +1)
        if dolls[leftPtr] == 1 :
            count -= 1
        leftPtr += 1
    else :
        rightPtr += 1
        if rightPtr < N and dolls[rightPtr] == 1 :
            count += 1

print(minLength if minLength != N else -1)