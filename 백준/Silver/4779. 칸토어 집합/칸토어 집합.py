def cantor(num):
  if num == 0:
    return "-"
  
  return cantor(num-1) + " " * (3**(num-1)) + cantor(num-1)

while True:
  try:
    N = int(input())
    print(cantor(N))
  except:
    break