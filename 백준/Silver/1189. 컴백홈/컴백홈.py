from collections import deque

R, C, K = map(int, input().split())

matrix = []
for _ in range(R):
  line = input()
  matrix.append(line)

matrix.reverse() # 왼쪽 위에서 오른쪽 아래로 변경

start = (0,0)
end = (R-1,C-1)

visited_set = set()
visited_set.add((0,0))
mv = [(0,1), (0,-1), (1,0), (-1,0)]
q = deque([(start, visited_set, 1)])

answer = 0
while q:
  cur, visited_set, distance = q.popleft()
  cur_row, cur_col = cur

  if cur == end:
    if distance == K:
      answer += 1
    continue

  for next_row_mv, next_col_mv in mv:
    next_row = cur_row + next_row_mv
    next_col = cur_col + next_col_mv

    if not (0 <= next_row < R and 0 <= next_col < C):
      continue

    if matrix[next_row][next_col] == "T":
      continue

    next = (next_row, next_col)
    if next in visited_set:
      continue 

    new_visited_set = visited_set.copy()
    new_visited_set.add(next)
    q.append((next, new_visited_set, distance+1))

print(answer)