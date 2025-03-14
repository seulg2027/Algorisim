'''
42839번 소수찾기

에라토스테네스의 체 오랜만!
순열라이브러리 기억하기
'''


import math
from itertools import permutations

def solution(numbers):
    answer = 0
    m = 10000000
    arr = [True for _ in range(m+1)]
    arr[0], arr[1] = False, False
    
    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(m)+1)):
        if arr[i] == True:
            j = 2
            while i * j <= m:
                arr[i*j] = False
                j += 1
    
    # 순열을 사용해 글자 개수 조합 만들어냄
    # 조합이 아닌 순열을 사용해야하는 이유 -> 같은 숫자의 조합이라도 순서가 다를 경우, 다른 숫자가 나오므로
    papers = []
    visited = set()
    for i in range(1, len(numbers)+1):
        papers.extend(list(permutations(list(numbers), i)))
    
    # 소수인지 검사하여 answer 냄
    for p in papers:
        num = ''.join(p)
        if not int(num) in visited:
            if arr[int(num)]:
                answer += 1
        visited.add(int(num))
    
    return answer