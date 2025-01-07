N = int(input())
numbers = list(map(int, input().split()))

dp = [1 for _ in range(N)] 
  
for i in range(N):
  number = numbers[i]
  for j in range(i):
    if numbers[j] < number:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))