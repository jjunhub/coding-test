import sys
input = sys.stdin.readline

def find_max_sticker_score() -> int :
  stickers = []
  n = int(input())
  stickers.append(list(map(int, input().split())))
  stickers.append(list(map(int, input().split())))
  
  memo = [[0 for i in range(n)] for _ in range(2)]
  
  memo[0][0] = stickers[0][0]
  memo[1][0] = stickers[1][0]

  if n > 1 :
    memo[0][1] = stickers[0][1] + memo[1][0]
    memo[1][1] = stickers[1][1] + memo[0][0]

  for idx in range(2, n):
    memo[0][idx] = stickers[0][idx] + max(memo[1][idx-1], memo[1][idx-2])
    memo[1][idx] = stickers[1][idx] + max(memo[0][idx-1], memo[0][idx-2])

  return max(memo[0][n-2], memo[0][n-1], memo[1][n-2], memo[1][n-1])
  
testcase = int(input())
for _ in range(testcase):
  print(find_max_sticker_score())
