N = int(input())
tropies = [ int(input()) for _ in range(N) ]

# Left Check
max_height = -1
left_count = 0
for idx in range(N):
  height = tropies[idx]
  if max_height < height:
    max_height = height
    left_count += 1
  else:
    continue

# Right Check
tropies.reverse()
max_height = -1
right_count = 0
for idx in range(N):
  height = tropies[idx]
  if max_height < height:
    max_height = height
    right_count += 1
  else:
    continue

print(left_count)
print(right_count)