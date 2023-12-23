list = []
count = [0] * (1000+1)
sum = 0

for t in range(1001):
    count.append

for i in range(10):
    list.append(int(input()))

for i in list:
    sum += i
    count[i] += 1

avg = int(sum / len(list))
    
print(avg)
print(count.index(max(count)))
