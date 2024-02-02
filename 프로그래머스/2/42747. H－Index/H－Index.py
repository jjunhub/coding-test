def solution(citations):
    h, idx = 0, 0
    citations.sort()
    print(citations)
    
    while True:
        print(f'h = {h}, idx = {idx}, citations[{idx}] = {citations[idx]} ')
        
        # Find Where is H in citations
        if h > citations[idx]:
            while h > citations[idx]:
                idx += 1
                if idx == len(citations):
                    break
                print(f'h = {h}, idx = {idx}, citations[{idx}] = {citations[idx]} ')
            
        # Check citations number that >= h
        if h <= len(citations) - idx:
            h += 1
        else:
            break
    return h-1

print('---')
print(solution([3,3,3,4]))
print('---')

