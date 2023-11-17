import sys
input = sys.stdin.readline

T  = int(input())

for _ in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  distanceBetweenTurret = ((x2 - x1)**2 + (y2 - y1) **2) ** (1/2)
  if r1 + r2 < distanceBetweenTurret : # case 1
    print(0)
  elif r1 + r2 == distanceBetweenTurret : # case 2
    print(1)
  else : # r1 + r2 > distanceBetweenTurret 
    if distanceBetweenTurret == 0 :
      if r1 == r2 :
        print(-1)
      else :
        print(0)
    else :
      if min(r1, r2) + distanceBetweenTurret == max(r1,r2) :
        print(1)
      elif min(r1, r2) + distanceBetweenTurret > max(r1, r2):
        print(2)
      else :
        print(0)
  
    