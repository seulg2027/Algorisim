'''
132265 롤케이크 자르기
'''

from collections import Counter

def solution(topping):
    answer = 0
    front = set([topping[0]])
    back = Counter(topping[1:])
    
    for i in range(1, len(topping)):
        front.add(topping[i])
        back[topping[i]] -= 1
        if back[topping[i]] == 0:
            back.pop(topping[i])
        if len(front) == len(back):
            answer += 1
    
    return answer