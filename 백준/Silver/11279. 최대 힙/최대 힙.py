import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
hp = list()
for _ in range(N):
  num = int(input())
  if num == 0 :
    if not hp :
      print(0)
    else :
      print((-1) * heappop(hp))

  else :
    heappush(hp, (-1) * num)