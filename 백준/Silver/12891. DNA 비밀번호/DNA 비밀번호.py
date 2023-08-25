import sys
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input().rstrip()
A, C, G, T = map(int, input().split())

result = {"A": A, "C": C, "G": G, "T": T}
answer = {"A": 0, "C": 0, "G": 0, "T": 0}
count = 0

for char in DNA[:P]:
    answer[char] += 1

if result["A"] <= answer["A"] and result["C"] <= answer["C"] and result["G"] <= answer["G"] and result["T"] <= answer["T"]:
    count += 1

leftPtr = 0
rightPtr = P
while(rightPtr < S):
    answer[str(DNA[leftPtr])] -= 1
    answer[str(DNA[rightPtr])] +=1
    if result["A"] <= answer["A"] and result["C"] <= answer["C"] and result["G"] <= answer["G"] and result["T"] <= answer["T"]:
        count += 1

    leftPtr += 1
    rightPtr += 1

print(count)
