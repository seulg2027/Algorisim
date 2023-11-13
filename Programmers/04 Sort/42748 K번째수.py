'''
K번째수
다시 풀어봄,, 생각없이 풀 수 있음
'''

def solution(array, commands):
    answer = []
    
    for c in commands:
        arr = sorted(array[c[0]-1:c[1]])
        answer.append(arr[c[2]-1])
    
    return answer