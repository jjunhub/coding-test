def check_is_answer(number):
  for i in number:
    if not (i == "4" or i == "7"):
      return False
  return True

N = input()
while True:
  if check_is_answer(N):
    break
  N = str(int(N) - 1)

print(N)