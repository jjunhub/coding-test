from itertools import permutations
def solution(numbers):
    answer = set()
    numbers = list(numbers)
    
    for length in range(1, len(numbers)+1):
        
        # Make All Combination
        for numberStrings in permutations(numbers, length):
            num = toIntType(numberStrings) # String List to One Integer
            
            if isPrimeNum(num): # Check the number is Prime Number
                answer.add(num)

    return len(answer) # Count Numbers

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
    