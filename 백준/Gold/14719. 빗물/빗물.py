H, W = map(int, input().split())
blocks = list(map(int, input().split()))
total_rain = 0

for target_idx in range(W):
  left_max_height = max(blocks[:target_idx+1])
  right_max_height = max(blocks[target_idx:])
  total_rain += max((min(left_max_height, right_max_height) - blocks[target_idx]), 0)

print(total_rain)