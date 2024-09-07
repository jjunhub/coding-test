import sys
from collections import deque
input = sys.stdin.readline

def bfs(s_r, s_c, t_r, t_c, l):
  matrix[s_r][s_c] = 1
  q = deque([(s_r, s_c, 0)])
  mv = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

  while q:
    now_r, now_c, times = q.popleft()
    if now_r == t_r and now_c == t_c:
      return times

    for i in range(8):
      next_r, next_c = now_r + mv[i][0], now_c + mv[i][1]

      if not ( 0 <= next_r < l and 0 <= next_c < l):
        continue
    
      if matrix[next_r][next_c] == 0:
        matrix[next_r][next_c] = 1
        q.append((next_r, next_c, times+1))

t = int(input())
for _ in range(t):
  l = int(input())
  matrix = [ [0 for _ in range(l)] for _ in range(l)]
  now_r, now_c = map(int, input().split())
  target_r, target_c = map(int, input().split())

  print(bfs(now_r, now_c, target_r, target_c, l))