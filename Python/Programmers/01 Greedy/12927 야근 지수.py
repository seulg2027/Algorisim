'''
가장 큰 수부터 작업 처리하기
-> 최대 힙 사용하기
'''
import heapq

def solution(n, works):
    works = list(-w for w in works)
    heapq.heapify(works)
    
    while n > 0:
        i = heapq.heappop(works)
        if i == 0:
            break
        heapq.heappush(works, i+1)
        n -= 1
    
    answer = sum(w*w for w in works)
    
    return answer