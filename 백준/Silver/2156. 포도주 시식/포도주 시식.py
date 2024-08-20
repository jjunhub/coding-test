N = int(input())

def find_max_drink(N) -> int:
  if N == 1 :
    return drink[0]
  
  dp = [ [0, 0, 0] for _ in range(N)]

  dp[0][0] = 0
  dp[0][1] = drink[0]
  dp[0][2] = drink[0]

  dp[1][0] = drink[0]
  dp[1][1] = drink[1]
  dp[1][2] = drink[0] + drink[1]

  for i in range(2, N):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = drink[i] + max(dp[i-2])
    dp[i][2] = drink[i] + dp[i-1][1]

  result = max(max(dp[N-1]), max(dp[N-2]))

  return result

drink = [0] * N

for idx in range(N):
  drink[idx] = int(input())

print(find_max_drink(N))