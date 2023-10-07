import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Numbers = list(map(int, input().split()))
NumbersWithIndex = []
for number in enumerate(Numbers, start=1):
  number = number 
  NumbersWithIndex.append(number)

deck = deque(NumbersWithIndex)

while(len(deck) != 1):
  popValue = deck.popleft()
  print(popValue[0], end= " ")
  if popValue[1] > 0 :
    deck.rotate((-1) * (popValue[1] - 1))
  else :
    deck.rotate((-1) * (popValue[1]))

print((deck.popleft())[0], end= " ")