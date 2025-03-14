'''
43236번 징검다리

너무 어려웠음..

1. 기준 mid 값을 잡고 기준보다 돌 사이의 거리가 짧다면 돌 제거 (DELETE에 추가)
2. 돌 사이의 거리가 더 길다면 현재 돌의 거리로 update
3. 최솟값 update
'''

def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    left = 0
    right = distance
    
    while left <= right:
        mid = (left + right) // 2
        delete_cnt = 0
        min_distance = 1e9
        now = 0
            
        for rock in rocks:
            dist = rock - now
            if dist <= mid:
                delete_cnt += 1
            else:
                now = rock
                min_distance = min(min_distance, dist)
            
        if delete_cnt > n:
            right = mid - 1
        else:
            answer = max(min_distance, answer)
            left = mid + 1
    
    return answer