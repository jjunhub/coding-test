import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deck = deque([])

for _ in range(N):
  명령 = input().rstrip()

  if len(명령) > 1:
    숫자, 정수 = map(int, 명령.split())
  else :
    숫자 = int(명령)
  
  if 숫자 == 1:
    deck.appendleft(정수)
  elif 숫자 == 2:
    deck.append(정수)
  elif 숫자 == 3:
    if deck:
      print(deck.popleft())
    else :
      print(-1)
  elif 숫자 == 4:
    if deck:
      print(deck.pop())
    else :
      print(-1)
  elif 숫자 == 5:
    print(len(deck))
  elif 숫자 == 6:
    if deck:
      print(0)
    else :
      print(1)
  elif 숫자 == 7:
    if deck:
      print(deck[0])
    else:
      print(-1)
  elif 숫자 == 8:
    if deck:
      print(deck[-1])
    else:
      print(-1)