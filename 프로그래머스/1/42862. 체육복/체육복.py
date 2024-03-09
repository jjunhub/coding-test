def solution(n, lost, reserve):
    
    clothes = [1] * (n+1) # clothes[0] is dummy
    clothes[0] = 0
    
    for hasExtraClothes in reserve:
        clothes[hasExtraClothes] += 1
    
    for hasStolenClothes in lost:
        clothes[hasStolenClothes] -= 1
        
    for stdNum in range( 1, n+1):
        # check has clothes
        if clothes[stdNum] > 0:
            continue
        # If had no clothes, check left one
        if clothes[stdNum-1] > 1:
            clothes[stdNum] += 1
            clothes[stdNum-1] -= 1
            continue    
        # check right one
        if stdNum+1 <= n and clothes[stdNum+1] > 1:
            clothes[stdNum] += 1
            clothes[stdNum+1] -= 1
            continue
    
    return clothes.count(1) + clothes.count(2)