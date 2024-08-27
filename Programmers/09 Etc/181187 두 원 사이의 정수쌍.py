'''
181187번 두 원 사이의 정수쌍

수학 문제
-> x or y축을 기준으로 교점 사이의 거리를 구하기
'''

import math

def solution(r1, r2):
    answer = 0
    
    for i in range(1, r2+1):
        if r1 > i:
            start = math.ceil(math.sqrt(math.pow(r1, 2) - math.pow(i, 2)))
        else:
            start = 0
        
        end = int(math.sqrt(math.pow(r2, 2) - math.pow(i, 2)))
        answer += end - start + 1
    
    return answer*4