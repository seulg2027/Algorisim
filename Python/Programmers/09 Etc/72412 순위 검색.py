'''
72412번 순위 검색

1번째 시도 - filter 로 한 번에 정렬함 (시간초과)
2번째 시도 - 스터디원 풀이 참고해서 bitmasking 사용
'''

from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    bit_masks = []
    
    def backtraking(size): # 비트마스킹..외우기..
        if size == 4:
            bit_masks.append(bit.copy())
            return
        bit.append(1)
        backtraking(size+1)
        bit[-1] = 0
        backtraking(size+1)
        bit.pop()
    
    bit = []
    backtraking(0) # 비트마스킹, 0은 있음 1은 없음
    info_dict = defaultdict(list)
    
    def fill_scores_dict(info_):
        for bit_mask in bit_masks:
            key = ""
            for i in range(4):
                key += info_[i] if bit_mask[i] else "-"
            info_dict[key].append(int(info_[-1]))
    
    for item in info:
        item = item.split(" ")
        fill_scores_dict(item)
    
    for k, v in info_dict.items(): # 먼저 정렬해준 뒤, query 계산하기
        v.sort()
    
    for q in query:
        condition = q.replace(" and "," ").split(" ")
        result = info_dict["".join(condition[:-1])]
        ans = bisect_left(result, int(condition[-1]))
        answer.append(len(result)-ans)
    
    return answer