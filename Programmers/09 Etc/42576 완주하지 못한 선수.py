'''
완주하지 못한 선수
* 집합 자료형을 사용할 줄 알았으나, 중복되는 값을 제거하는 게 아님
* 중복되는 값도 갯수를 세어야 하므로 딕셔너리 활용
'''

def solution(participant, completion):
    part_dict = dict()
    comp_dict = dict()
    answer = ''
    
    for p in participant:
        if p in part_dict.keys():
            part_dict[p] += 1
        else:
            part_dict[p] = 1
    
    for p in completion:
        if p in comp_dict.keys():
            comp_dict[p] += 1
        else:
            comp_dict[p] = 1
    
    for person in participant:
        if person not in comp_dict.keys() or part_dict[person] != comp_dict[person]:
            answer = person
            break
    
    return answer