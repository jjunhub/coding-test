import sys
input = sys.stdin.readline

_dict = {}
count = 0
while True:
    sample = input().rstrip()
    if sample == "":
        break
    if sample not in _dict:
        _dict[sample] = 1
    else :
        _dict[sample] += 1
    
    count += 1

names = list(_dict.keys())
names.sort()

for name in names:
    print("%s %.4f" % (name, _dict[name]/count*100))
    