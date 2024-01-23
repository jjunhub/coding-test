galhos = list(input())

pipe = 0
result = 0

for idx in range(len(galhos)):
  if galhos[idx] == "(" and idx + 1 < len(galhos) and galhos[idx+1] == ")" :
    result += pipe
    galhos[idx+1] = "-"
  elif galhos[idx] == "(" :
    pipe += 1
  elif galhos[idx] == ")" :
    pipe -= 1
    result += 1
  
print(result)
