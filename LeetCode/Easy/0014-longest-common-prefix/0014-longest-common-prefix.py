# STEP 0. 제약조건 확인 - 단어 200개, 단어는 모두 200자 이하 ( 200 * 200 -> N^2 가능 )
# STEP 1. 가장 짧은 단어 길이 찾기 - loop로 O(N * 1)에 구하기 가능. len 함수는 O(1)이므로
# STEP 2. idx 1씩 늘려가면서 정답 찾기
###########
def find_min_len_str(strs: List[str]) -> int:
    min_len = 201
    for s in strs:
        min_len = min(min_len, len(s))
    return min_len

def find_longest_prefix(strs: List[str], max_prefix_len: int) -> str:
    answer = list()
    for idx in range(max_prefix_len):
        temp_prefix_part = ""
        for s in strs:
            if temp_prefix_part == "":
                temp_prefix_part = s[idx]
            
            if temp_prefix_part != s[idx]:
                return "".join(answer)
        answer.append(s[idx])
    return "".join(answer)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # STEP 1.
        min_len = find_min_len_str(strs)

        # STEP 2.
        return find_longest_prefix(strs, min_len)