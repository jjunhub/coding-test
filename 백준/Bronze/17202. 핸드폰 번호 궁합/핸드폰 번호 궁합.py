import sys
input = sys.stdin.readline

A_number = input().rstrip()
B_number = input().rstrip()
newStr = ""

for i in range(len(A_number)):
    newStr += A_number[i] + B_number[i]

while len(newStr) > 2 :
    tempStr = ""
    for i in range(len(newStr) - 1):
        tempStr += str((int(newStr[i]) + int(newStr[i+1])) % 10)
    newStr = tempStr
    
print(newStr)