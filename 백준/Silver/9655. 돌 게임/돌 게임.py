N = int(input())

def checkWho(data):
  if data == "SK":
    return "CY"
  else :
    return "SK"

result = [0] * (N+4)
result[1] = "SK"
result[2] = "CY"
result[3] = "SK"

for i in range(1, N):
  if result[i+1] == 0:
    result[i+1] = checkWho(result[i])
  if result[i+3] == 0:
    result[i+3] = checkWho(result[i])


print(result[N])