import sys
from heapq import heappush, heappop
input = sys.stdin.readline
POSTIVIE = 1
NEGATIVE = -1

N = int(input())
hq = list()
for _ in range(N):
  num = int(input())

  if num != 0:
    if num > 0 :
      heappush(hq, (num + 0.1, POSTIVIE))
    else :
      heappush(hq, ((NEGATIVE) * num - 0.1, NEGATIVE))
  else:
    if not hq :
      print(0)
    else :
      num, sign = heappop(hq)
      
      if sign == POSTIVIE:
        print(int(num))
      else :
        print((int((num+0.5)*NEGATIVE)))