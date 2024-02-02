def solution(citations):
    h, idx = 0, 0
    citations.sort()
    
    while True:
        # Find Where is H in citations
        if h > citations[idx]:
            while h > citations[idx]:
                idx += 1
                if idx == len(citations):
                    break
                    
        # Check citations number that >= h
        if h <= len(citations) - idx:
            h += 1
        else:
            break
    
    # Get Max h
    return h - 1

