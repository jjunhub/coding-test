import sys
input = sys.stdin.readline

stair_number = int(input())
scores = [0] * 301
dp = [[ 0 for i in range(3) ] for _ in range(302)]

for i in range(1, stair_number+1):
    scores[i] = int(input())

dp[1][1] = dp[1][2] = scores[1]
dp[2][1] = scores[2]
dp[2][2] = scores[1] + scores[2]


for i in range(3, stair_number+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + scores[i]
    dp[i][2] = dp[i-1][1] + scores[i]
    # print(f'dp[{i}][1] = {dp[i][1]} dp[{i}][2] = {dp[i][2]}')

print(max(dp[stair_number][1], dp[stair_number][2]))