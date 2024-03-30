import sys
input = sys.stdin.readline

N, D = map(int, input().split())

arr = [ [] for _ in range(D+1)]

for _ in range(N):
  start, end, dist = map(int, input().split())
  if end > D : continue
  arr[start].append([end, dist])

way = [ i for i in range(D+1)]

for pos in range(D+1):
  if pos != 0:
    way[pos] = min(way[pos], way[pos-1]+1)
  
  for end, dist in arr[pos]:
    if way[end] > dist + way[pos]:
      way[end] = dist + way[pos]

print(way[D])