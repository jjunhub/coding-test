def solution(friends, gifts):
    answer = 0
    gift_dict = make_gift_dict(friends)
    gift_dict = apply_gifts_history(gift_dict, gifts)
    gift_score = caculate_gift_score(gift_dict)
    answer = find_max_gift_receieve(gift_dict, gift_score)
    return answer

def make_gift_dict(friends : list) -> dict:
    # friend들간의 선물 기록을 파악하기 위한 딕셔너리 구현
    gift_dict = dict()
    for friend_give in friends:
        gift_dict[friend_give] = dict()
        for friend_receive in friends:
            if friend_give == friend_receive:
                continue
            gift_dict[friend_give][friend_receive] = [0, False]
            # dic[받는 이] = [ 준 개수-받은 개수, 주고 받은 경험 ]
    return gift_dict

def apply_gifts_history(gift_dict : dict, gifts : list) -> dict:
    for gift in gifts:
        give, receive = gift.split(" ")
        gift_dict[give][receive][0] += 1 # 준 개수 더하기
        gift_dict[receive][give][0] -= 1 # 받은 개수 빼기

        gift_dict[receive][give][1] = True # 주고 받은 기록 추가
        gift_dict[give][receive][1] = True # 주고 받은 기록 추가
    return gift_dict
        
def caculate_gift_score(gift_dict : dict) -> dict:
    gift_score = dict()
    
    # 주고 받은 기록 집계
    for give in gift_dict.keys():
        gift_score[give] = 0
        for receive in gift_dict[give].keys():
            if gift_dict[give][receive][1] == False:
                continue
            gift_score[give] += gift_dict[give][receive][0]
    
    return gift_score

def find_max_gift_receieve(gift_dict, gift_score):
    max_gift_receive = -1
    for give in gift_dict:
        temp_gift_receive = 0
        for receive in gift_dict[give].keys():
            if gift_dict[give][receive][1] == False or gift_dict[give][receive][0] == 0:
                give_gift_score = gift_score[give]
                receive_gift_score = gift_score[receive]
                if give_gift_score == receive_gift_score:
                    continue
                temp_gift_receive += 1 if give_gift_score > receive_gift_score else 0
            else:
                temp_gift_receive += 1 if gift_dict[give][receive][0] > 0 else 0
        max_gift_receive = max(temp_gift_receive, max_gift_receive)
    return max_gift_receive
                
                
                
            