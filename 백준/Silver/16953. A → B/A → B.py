from collections import deque

def bfs(start):
  q = deque([(start, 0)])
  visited = set()
  visited.add(start)

  while q:
    now, times = q.popleft()
    if now == target:
      return times + 1
    
    for next in (now*2, now*10 + 1) :
      if next not in visited and next <= target:
        q.append((next, times+1))
        visited.add(next)
      
  return -1

start, target = map(int, input().split())
print(bfs(start))