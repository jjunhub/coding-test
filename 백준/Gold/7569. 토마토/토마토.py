from collections import deque

M, N, H = map(int, input().split())

matrix = [ [list(map(int, input().split())) for _ in range(N)] for _ in range(H) ]
q = deque()

mv = [ (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), ( -1, 0, 0) ]

for h in range(H):
  for n in range(N):
    for m in range(M):
      if matrix[h][n][m] == 1:
        q.append((h,n,m,0))

while q:
  now_h, now_n, now_m, day = q.popleft()

  for dh, dn, dm in mv:
    next_h, next_n, next_m = now_h + dh, now_n + dn, now_m + dm
    if not (0 <= next_h < H and 0<= next_n < N and 0<= next_m < M):
      continue
      
    if matrix[next_h][next_n][next_m] == 0:
      matrix[next_h][next_n][next_m] = 1
      q.append((next_h, next_n, next_m, day+1))

mature = True
for h in range(H):
  for n in range(N):
    for m in range(M):
      if matrix[h][n][m] == 0:
        mature = False

if mature:
  print(day)
else:
  print(-1)