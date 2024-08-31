T = int(input())    

Abutton = T // 300
T = T % 300

Bbutton = T // 60
T = T % 60

Cbutton = T // 10
T = T % 10

if T == 0:
  print(Abutton, Bbutton, Cbutton)
else :
  print(-1)