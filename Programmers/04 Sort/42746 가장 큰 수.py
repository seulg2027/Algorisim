'''
가장 큰 수
'''

def solution(numbers):
    answer = ''
    
    numbers_sort = []
    for num in numbers:
        numbers_sort.append(str(num))
    numbers_sort.sort(key=lambda x: x*3, reverse=True) # *3은 개수를 3배한것!!
    
    for j in numbers_sort:
        answer += ''.join(j)
    answer = str(int(answer)) # 모든 numbers원소가 0일 경우를 대비해서
    
    return answer