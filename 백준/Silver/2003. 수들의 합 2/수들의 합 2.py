import sys
input = sys.stdin.readline

N, target = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
right = 1 
count = 0

while(left <= right and right <= len(numbers)) :
    sumOfNum = numbers[left:right] # left부터 right까지의 숫자들만 가져옴
    hap = sum(sumOfNum)

    if(hap < target) : right += 1
    elif(hap > target) : left += 1
    else : 
        count += 1
        right += 1

print(count)