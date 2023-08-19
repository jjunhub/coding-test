import sys
input = sys.stdin.readline

N = int(input())
dict = {}

for _ in range(N):
    filename = input().rstrip()
    extension = filename.split(".")[1]
    if extension in dict :
        dict[extension] += 1
    else :
        dict[extension] = 1
    
key_value = []

for key in dict:
    key_value.append(key)

key_value.sort()

for key in key_value:
    print(key, dict[key])
