import sys
from collections import deque

input = sys.stdin.readline
deck = deque()

N = int(input())
for number in range(1,N+1):
  deck.append(number)

while(len(deck) >= 2):
  trash = deck.popleft()
  if len(deck) == 1 :
    break
  reuse = deck.popleft()
  deck.append(reuse)

print(deck.popleft())