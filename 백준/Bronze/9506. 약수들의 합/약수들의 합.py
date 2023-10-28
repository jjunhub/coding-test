while True:
  n = int(input())
  if n == -1 :
    break
  yaksu = []
  for i in range(1, n):
    if n % i == 0:
      yaksu.append(i)

  if sum(yaksu) == n:
    yaksu = list(map(str, yaksu))
    print(n,"=", end =" ")
    print(" + ".join(yaksu))
  else :
    print(n, "is NOT perfect.")