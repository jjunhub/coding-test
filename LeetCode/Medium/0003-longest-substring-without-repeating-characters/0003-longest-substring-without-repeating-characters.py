class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # 가장 앞에서부터 문자열을 읽는다.
        # 새로운 문자가 기존에 읽은 것인지 판단하는 게 중요하다. -> 해시 구조가 필요
        # 중간 중간에, 문자열이 겹치는거면은 새로운 문자열을 파야함.
        
        max_len = 0
        temp_len = 0
        valid_ptr = -1
        char_dict = dict()

        for idx, char in enumerate(s, 0):
            if char in char_dict:
                # valid_ptr과 비교해서, 더 작은 값이라면 패스하고 새로 추가한다.
                if valid_ptr > char_dict[char]:
                    char_dict[char] = idx
                    temp_len += 1
                else :# valid_ptr과 비교해서, 더 큰 값이라면 valid_ptr을 char_dict에 있는 값+1로 바꿈, max_len도 바꿈
                    temp_len = idx - char_dict[char]
                    valid_ptr = char_dict[char] + 1
                    char_dict[char] = idx
            else :
                # char_dict에 추가하고, max_len도 바꿈
                char_dict[char] = idx
                temp_len += 1
            max_len = max(max_len, temp_len)
    
        return max_len
        