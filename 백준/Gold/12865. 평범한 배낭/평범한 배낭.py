def sol():
  N, K = map(int, input().split())
  items = [ tuple(map(int, input().split())) for _ in range(N)]
  dp = [0] * (K+1)

  for w, v in items:
    for j in range(K, w-1, -1):
      dp[j] = max(dp[j], dp[j-w] + v)

  print(dp[K])

sol()