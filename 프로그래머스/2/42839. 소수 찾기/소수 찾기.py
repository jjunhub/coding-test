from itertools import permutations
def solution(numbers):
    answer = set()
    # make all number
    numbers = list(numbers)
    print(numbers)
    
    for length in range(1, len(numbers)+1):
        for numberStrings in permutations(numbers, length):
            num = toIntType(numberStrings)
            if isPrimeNum(num):
                answer.add(num)

    return len(answer)

def isPrimeNum(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def toIntType(numberStrings):
    num = ""
    for numberString in numberStrings:
        num += numberString
    return int(num)
    