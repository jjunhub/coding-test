import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

N = int(input())
minHeap = list()
heapify(minHeap)

for _ in range(N):
  number = int(input())
  if number == 0:
    if len(minHeap) > 0 :
      print(heappop(minHeap))
    else :
      print(0)

  else :
    heappush(minHeap, number)