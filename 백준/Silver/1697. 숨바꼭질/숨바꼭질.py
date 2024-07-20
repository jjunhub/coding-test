from collections import deque

def bfs(start, target):
  q = deque() # position, time
  q.append((start,0))
  visited = set()
  visited.add(start)

  while q:
    pos, time = q.popleft()
    if pos == target:
      return time

    # X - 1
    if pos-1 >= 0 and (pos-1 not in visited):
      visited.add(pos-1)
      q.append((pos-1, time+1))

    # X + 1
    if pos+1 <= 100000 and (pos+1 not in visited):
      visited.add(pos+1)
      q.append((pos+1, time+1))

    # 2 * X
    if 2*pos <= 100000 and (pos*2 not in visited):
      visited.add(pos*2)
      q.append((pos*2, time+1))

N, K = map(int, input().split())
print(bfs(N,K))