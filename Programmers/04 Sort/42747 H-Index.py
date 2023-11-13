'''
H-index
'''

def solution(citations):
    answer = 0
    citations.sort()
    
    for c in range(10000, -1, -1):
        citations_list = [i for i in citations if i >= c]
        Hidx = len(citations_list)
        if c <= Hidx:
            answer = c
            break
    
    return answer
