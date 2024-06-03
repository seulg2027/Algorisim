'''
2805번 나무자르기

filter, map 함수 활용 똑똑하게 하기
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        # 자를 높이보다 높은 나무만 가져와서 자르기
        some_trees = list(filter(lambda x: x>mid, trees))
        sum_height = sum(map(lambda x: x-mid, some_trees))
        
        if sum_height == M:
            return mid
        elif sum_height > M:
            start = mid + 1
        elif sum_height < M:
            end = mid - 1
    
    # 만약 딱 맞는 높이가 없다면,,
    # 목표 길이보다 길다면 그냥 mid 값 반환하기
    if sum_height > M:
        return mid
    else:
        return mid-1

print(binary_search(1, max(trees)))