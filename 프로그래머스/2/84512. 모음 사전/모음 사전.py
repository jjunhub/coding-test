def solution(word):
    answer = 0
    alphabets = ["A", "E", "I", "O", "U"]
    for val, alpha in enumerate(alphabets, start = 1):
        word = word.replace(alpha, str(val))
    word = list(map(int, word))
    
    val = [781, 156, 31, 6, 1]
        
    for idx, w in enumerate(word):
        answer += val[idx] * (w-1) + 1
        
    return answer