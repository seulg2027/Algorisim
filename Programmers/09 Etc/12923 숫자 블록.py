'''
12923번 숫자 블록

숫자 제한사항 때문에 애를 먹었던..
'''

import math

def solution(begin, end):
    answer = []
    
    for n in range(begin, end+1):
        if n == 1:
            answer.append(0)
            continue
        
        max_value = 1
        # 가장 큰 약수 구하기
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n // i <= 10000000:
                    max_value = n // i # 가장 큰 값
                    break
                max_value = max(max_value, i)
        
        answer.append(max_value)
    
    return answer