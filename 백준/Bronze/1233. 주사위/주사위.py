from collections import defaultdict
S1, S2, S3 = map(int, input().split())
result = defaultdict(int)

for s1 in range(1, S1+1):
  for s2 in range(1, S2+1):
    for s3 in range(1, S3+1):
      result[s1+s2+s3] += 1

max_value = -1
answer = 0

for key, value in result.items():
  if max_value < value:
    max_value = value
    answer = key

print(answer)