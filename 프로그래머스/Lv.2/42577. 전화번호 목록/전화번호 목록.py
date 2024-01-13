import collections
def solution(phone_book):
    _dict = collections.Counter(phone_book)
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in _dict:
                return False
    
    return True