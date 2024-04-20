import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

dct = defaultdict(list)

for _ in range(M):
  A, B = map(int,input().split())
  dct[A].append(B)

startCity = X
queue = deque([])
queue.append( (X,0) )
visited = { X }
answer = [ ]

while queue:
  nowCity, distance = queue.popleft()
  if distance == K:
    answer.append(nowCity)

  for city in dct[nowCity]:
    if city not in visited:
      queue.append((city, distance + 1))
      visited.add(city)

if answer :
  answer.sort()
  for city in answer:
    print(city)
else :
  print(-1)