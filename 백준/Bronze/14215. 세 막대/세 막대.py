import sys
input = sys.stdin.readline

막대들 = list(map(int, input().split()))
막대들.sort()

def solution():
  if 막대들[2] >= 막대들[1] + 막대들[0]:
    return ( 막대들[1]+막대들[0] ) * 2 - 1
  else :
    return sum(막대들)
  
print(solution())