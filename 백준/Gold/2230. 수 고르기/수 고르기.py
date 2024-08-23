import sys
input = sys.stdin.readline
MAX_DIFF = 2 * 10e9

N, M = map(int, input().split())
numbers = [ int(input()) for _ in range(N)]
numbers.sort()

leftPtr = 0
rightPtr = 1
answer = MAX_DIFF

while rightPtr < N:
  diff = numbers[rightPtr] - numbers[leftPtr]

  if diff > M: # 차이가 클 때
    answer = min(answer, diff) 
    leftPtr +=1 
    rightPtr = rightPtr + 1 if leftPtr == rightPtr else rightPtr
  elif diff < M: # 차이가 작을 때,
    rightPtr +=1
  else :
    answer = diff
    break

print(answer)