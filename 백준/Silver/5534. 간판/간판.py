import sys
input = sys.stdin.readline

N = int(input())
name = input().rstrip()
count = 0

def solve(oldName, name):
  for indent in range(len(oldName)):
    for index, char in enumerate(oldName):
     if char == name[0]:
        flag = 1
        while(flag < len(name) and index + (indent+1) * flag < len(oldName) and ( oldName[index + (indent+1) * flag] == name[flag])):
           flag+=1

        if flag == len(name):
          return 1
  return 0


for _ in range(N):
    oldName = input().rstrip()
    count += solve(oldName, name)

print(count)