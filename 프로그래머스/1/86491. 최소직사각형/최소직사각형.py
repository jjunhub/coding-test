def solution(sizes):    
    maxGaro, maxSero = 0, 0

    for size in sizes:
        size.sort() # size[0]: garo, size[1]: sero
        if maxGaro < size[0]:
            maxGaro = size[0]
        if maxSero < size[1]:
            maxSero = size[1]
    
    return maxGaro * maxSero