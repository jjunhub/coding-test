import sys
input = sys.stdin.readline

N = int(input())
Members = []

for i in range(N):
  Member = input().split()
  Member[0] = int(Member[0])
  Members.append(Member)

Members.sort(key = lambda x : (x[0]))
for age,name in Members:
  print(age, name)