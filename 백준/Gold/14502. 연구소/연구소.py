import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def bfs(start_list : set, visited : set) -> int:
  q = deque(start_list)
  q.extend(start_list)
  visited.update(start_list)
  danger_space = 0

  mv = [(1, 0), (-1, 0), (0, -1), (0, 1)]

  while q:
    now_hang, now_yeol = q.popleft()

    for d in range(4):
      next_hang, next_yeol = now_hang + mv[d][0], now_yeol + mv[d][1]

      if not (0 <= next_hang < hang and 0 <= next_yeol < yeol) :
        continue

      if matrix[next_hang][next_yeol] == 0 and (next_hang, next_yeol) not in visited:
        q.append((next_hang, next_yeol))
        visited.add((next_hang, next_yeol))
        danger_space += 1
  
  return danger_space

hang, yeol = map(int, input().split())
matrix = list()
wall_set = set()
virus_set = set()
empty_set = set()

for _ in range(hang):
  one_row = list(map(int, input().split()))
  matrix.append(one_row)

for h in range(hang):
  for y in range(yeol):
    if matrix[h][y] == 0 : # empty
      empty_set.add((h,y))
    elif matrix[h][y] == 1 : # wall
      wall_set.add((h,y))
    else : # virus
      virus_set.add((h,y))

total_space = len(empty_set) - 3
safe_space = 0

for walls in combinations(empty_set, 3): # choose 3 wall from empty set
  for h, y in walls:
    matrix[h][y] = 1
  danger_space = bfs(virus_set, set())
  safe_space = max(total_space - danger_space, safe_space)
  for h, y in walls:
    matrix[h][y] = 0

print(safe_space)