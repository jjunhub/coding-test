from collections import deque
MAX_RANGE = 100001

def bfs(start, target) -> int:
  queue = deque()
  queue.append((start,0)) # (position, time)

  while queue:
    now_position, time = queue.popleft()
    if now_position == target:
      return time

    # 2배 순간이동
    multiple_twice = now_position
    while multiple_twice * 2 < MAX_RANGE:
      multiple_twice *= 2
      
      if visited[multiple_twice] != -1 : # 이미 방문
        break

      visited[multiple_twice] = time
      queue.append((multiple_twice, time))
  
    # -1, +1 이동
    for next_position in (now_position-1, now_position+1):
      if not 0 <= next_position < MAX_RANGE :
        continue

      if visited[next_position] == -1:
        visited[next_position] = time+1
        queue.append((next_position, time+1))

N, K = map(int, input().split())
visited = [-1] * (MAX_RANGE)
visited[N] = 0

print(bfs(N, K))