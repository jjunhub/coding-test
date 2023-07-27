import sys
input = sys.stdin.readline

A, B = map(int, input().split())

ListA = list(map(int, input().split()))
ListB = list(map(int, input().split()))

ptrA = 0
ptrB = 0

SizeA = len(ListA)
SizeB = len(ListB)
result = []

while ptrA < SizeA and ptrB < SizeB :
    if ListA[ptrA] < ListB[ptrB]:
        result.append(ListA[ptrA])
        ptrA += 1
    else :
        result.append(ListB[ptrB])
        ptrB += 1

if ptrA == SizeA : # B 리스트가 남아있을 때
    result.extend(ListB[ptrB:])
else : # A 리스트가 남아있을 때
    result.extend(ListA[ptrA:])

print(*result)