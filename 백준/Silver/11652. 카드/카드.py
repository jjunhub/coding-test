import sys
input = sys.stdin.readline

N = int(input())
dct = dict()
for _ in range(N):
  number = int(input())
  if number in dct:
    dct[number] += 1
  else:
    dct[number] = 1

ans_val = -1
ans_key = 0
for key, value in dct.items():
  if value > ans_val:
    ans_key = key
    ans_val = value
  elif value == ans_val:
    ans_key = min(ans_key, key)

print(ans_key)