from collections import defaultdict

N, M = input().split()

result = 0
M_dict = defaultdict(int)

for number in M:
  M_dict[int(number)] += 1

for base in N:
  base = int(base) # N
  for idx in range(0, 10):
    result += base * M_dict[idx] * idx

print(result)