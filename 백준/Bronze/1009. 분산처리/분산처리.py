import sys
input = sys.stdin.readline

T = int(input())

square_sheet = [
    [0],
    [1],
    [2,4,8,6],
    [3,9,7,1],
    [4,6],
    [5],
    [6],
    [7,9,3,1],
    [8,4,2,6],
    [9,1],
    [10],
]

for _ in range(T):
    a, b = map(int, input().split())
    a = 10 if a % 10 == 0 else a % 10
    b_index = b % len(square_sheet[a])
    b_index = b_index if b_index != 0 else len(square_sheet[a])
    result = square_sheet[a][ b_index - 1 ]
    print(result)