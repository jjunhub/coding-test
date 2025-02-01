N = int(input())
li = [0] * 1001
max_idx = -1
max_H = -1

for _ in range(N):
  idx, H = map(int, input().split())
  li[idx] = H
  
  if max_H < H:
    max_H = H
    max_idx = idx

area = max_H

max_H = -1
for idx in range(0, max_idx):
  if li[idx] > max_H:
    max_H = li[idx]
  
  area += max_H

max_H = -1
for idx in range(1000, max_idx, -1):
  if li[idx] > max_H:
    max_H = li[idx]
  
  area += max_H

print(area)