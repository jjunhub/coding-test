def solution(numbers, target):
    answer = []
    
    def fun(val, next_idx):
        # print(f'fun({val}, {next_idx})')
        if next_idx == len(numbers):
            if val == target:
                answer.append(0)
            return
        fun(val + numbers[next_idx], next_idx+1)
        fun(val - numbers[next_idx], next_idx+1)
    
    fun(0, 0)
    
    return len(answer)