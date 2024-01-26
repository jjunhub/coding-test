def solution(prices):
    len_ = len(prices)
    answer = [0] * len_
    stack = []
    for el in enumerate(prices):
        idx, nowPrice = el        
        
        if not stack or stack[-1][1] <= nowPrice:
            stack.append(el)
        else : # stack[-1][1] > price
            while stack and stack[-1][1] > nowPrice: 
                beforeidx, _ = stack.pop()
                answer[beforeidx] = idx - beforeidx 
            stack.append(el)
                
    while stack:
        idx, val = stack.pop()
        answer[idx] = len_ - 1 - idx
            
    return answer