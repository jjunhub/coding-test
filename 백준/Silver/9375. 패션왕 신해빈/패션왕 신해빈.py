import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    _dict = {}
    for _ in range(n):
        value, key = input().rstrip().split()
        if key in _dict:
            _dict[key] += 1
        else :
            _dict[key] = 1
    
    fashion = 1
    for key in _dict:
        fashion *= _dict[key] + 1

    fashion -= 1
    print(fashion)