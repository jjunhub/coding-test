import sys
input = sys.stdin.readline

A, B = map(int, input().split())

ListA = list(map(int, input().split()))
ListB = list(map(int, input().split()))

ptrA = 0
ptrB = 0

SizeA = len(ListA) # 2개 입력하면 2까지 나옴
SizeB = len(ListB)
result = []

for _ in range(SizeA + SizeB):
    if ptrA == SizeA :
      result.append(ListB[ptrB])
      ptrB += 1
    elif ptrB == SizeB :
      result.append(ListA[ptrA])
      ptrA += 1
    else :
      if ListA[ptrA] > ListB[ptrB] :
          result.append(ListB[ptrB])
          ptrB += 1
      else :
          result.append(ListA[ptrA])
          ptrA += 1

print(*result)