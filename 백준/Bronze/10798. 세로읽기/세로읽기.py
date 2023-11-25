import sys
input = sys.stdin.readline

li = []
for _ in range(5):
  li.append(input().rstrip())

for i in range(15):
  for j in range(5):
    if i < len(li[j]):
      print(li[j][i], end="")