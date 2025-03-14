'''
42890번 후보키

유일성까진 너무 쉬웠으나 최소성 조건을 대체 어떻게 세워야할지 몰라서 틀림
* 후보키 최소성 조건
=> 유일성을 만족하는 슈퍼키들 중에서 한 슈퍼키가 다른 슈퍼키의 부분집합이 되지 않으면 최소성을 만족하는 것이다.
'''

# 내가 푼 코드
from itertools import combinations

def solution(relation):
    answer = 0
    
    column_list = list(map(list, zip(*relation))) # 칼럼 기준
    candidate_col = [i+1 for i in range(len(column_list))]
    candidate_key = set()
    keys = [0] * (len(column_list)+1)
    
    for c in range(len(column_list)): # 유일성 만족
        col_set = set(column_list[c])
        if len(col_set) == len(column_list[c]):
            keys[c+1] = 1
            candidate_key.add(c+1)
    
    for i in range(2, len(column_list)): # 최소성 만족
        com = list(combinations(candidate_col, i))
        com_list = list(combinations(column_list, i))
        for j in range(len(com)): # 조합 하나하나 체크하기
            is_valid = True
            key = []
            for z in range(i): # 하나의 조합에서
                if com[j][z] in candidate_key or keys[com[j][z]] == 1:
                    is_valid = False
                    break
            if is_valid:
                col = list(map(tuple, zip(*com_list[j])))
                if len(col) == len(set(col)):
                    for m in com[j]:
                        keys[m] = 1
                    candidate_key.update([com[j]])
                
    answer = len(candidate_key)
    
    return answer

# 다른 사람의 코드,, 으렵다
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
        
    #유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성,, 부분집합이면 False로 바꿔줌
                    put = False
                    break
                    
            if put: unique.append(i)
    
    return len(unique)
