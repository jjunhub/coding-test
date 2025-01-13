N = int(input())
miro = list(map(int, input().split()))

dp = [1000] * N
dp[0] = 1

for idx in range(N):
  can_move = miro[idx]
  for j in range(1, can_move+1):
    if idx + j >= N : continue
    dp[idx + j] = min(dp[idx+j], dp[idx]+1)
  
if dp[-1] == 1000:
  print(-1)
else:
  print(dp[-1]-1)