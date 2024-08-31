import sys
from heapq import heappop, heappush
input = sys.stdin.readline
heap = []

N = int(input())
homeworks = [ list(map(int, input().split()))  for _ in range(N)]
homeworks.sort() # (deadline, cost)

for deadline, cost in homeworks:
  if deadline == len(heap):
    if heap[0] < cost:
      heappop(heap)
      heappush(heap, cost)
  else:
    heappush(heap, cost) 

print(sum(heap))