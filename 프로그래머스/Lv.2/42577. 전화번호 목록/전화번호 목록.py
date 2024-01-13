from collections import Counter
def solution(phone_book):
    _dict = Counter(phone_book)
    
    for phone in phone_book:
        prefix = ""
        for number in phone[:-1]:
            prefix += number
            if prefix in _dict:
                return False
    
    return True