N = input()
_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

for i in N:
    if i == '6' or i == '9':
        _dict['6'] += 0.5
    else :
        _dict[i] += 1
max_count = max(_dict.values())
print(int(max_count + 0.5))