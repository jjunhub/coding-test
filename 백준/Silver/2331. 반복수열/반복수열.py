A, P = map(int, input().split())
sequence = []
dict = { A : 1}
sequence.append(A)
while(True):
    number = str(sequence[-1])
    tempSum = 0
    for num in number:
        tempSum += int(num) ** P
        
    if tempSum in dict :
        dict[tempSum] += 1
        if dict[tempSum] == 3:
            break
    else :
        dict[tempSum] = 1
    sequence.append(tempSum)

result = 0
for num in dict:
    if(dict[num] < 2):
        result +=1

print(result)