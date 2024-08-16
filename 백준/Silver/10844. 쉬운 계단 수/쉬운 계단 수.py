N = int(input())

memo = [[0 for _ in range(10)] for _ in range(N)]

for i in range(1, 10):
  memo[0][i] = 1

for idx in range(1, N):
  memo[idx][0] = memo[idx-1][1]
  memo[idx][9] = memo[idx-1][8]
  for j in range(1, 9):
    memo[idx][j] = memo[idx-1][j-1] + memo[idx-1][j+1]

print(sum(memo[N-1]) % 1000000000)