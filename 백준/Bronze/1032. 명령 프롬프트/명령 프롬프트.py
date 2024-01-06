import sys

n = int(input())

result = []
for i in range(n):
  word = list(input().rstrip())
  if not result :
    result = word
  else :
    for idx in range(len(result)):
      if result[idx] != word[idx]:
        result[idx] = "?"

print("".join(result))