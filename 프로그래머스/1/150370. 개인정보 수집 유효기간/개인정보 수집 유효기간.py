def solution(today, terms, privacies):
    answer = []
    term_dict = get_term_dict(terms)
    
    for number, privacy in enumerate(privacies, 1):
        if is_expired_privacy(today, privacy, term_dict):
            answer.append(number)
    return answer

def is_expired_privacy(target_date, privacy, term_dict) -> bool:
    collected_date, term_type = privacy.split(" ")
    valid_duration = term_dict[term_type]
    valid_date = get_date_after(collected_date, valid_duration)
    print(valid_date)
    return is_after_date(valid_date, target_date)

def get_date_after(date, duration) -> str:
    year, month, day = date.split(".")
    month = int(month) + int(duration)
    if month > 12:
        year = int(year) + (month // 12)
        if month % 12 == 0:
            month = 12
            year -= 1
        else :
            month = month % 12
    return ".".join([str(year), str(month), day])

def is_after_date(valid_date, target_date) -> bool:
    valid_year, valid_month, valid_day = valid_date.split(".")
    target_year, target_month, target_day = target_date.split(".")            
    
    if int(valid_year) < int(target_year):
        return True
    elif int(valid_year) == int(target_year):
        if int(valid_month) < int(target_month):
            return True
        elif int(valid_month) == int(target_month):
            if int(valid_day) <= int(target_day):
                return True
    return False

def get_term_dict(terms) -> dict:
    term_dict = dict()
    for t in terms:
        term_type, valid_duration = t.split(" ")
        term_dict[term_type] = int(valid_duration)
    return term_dict