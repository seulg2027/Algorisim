'''
17266 어두운 굴다리

조건대로 구현

1) 범위 내에서 길이 구하기
    0~5 까지의 길에서 가로등이 2, 4에 있다면
    [2, 2, 1]
    (0~가로등1, 가로등1~가로등2, 가로등2~5)
2) 그 중 가로등 길이가 가장 많이 필요한 것 구하기

'''

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
spotlights = list(map(int, input().split()))
road_len = []

# 각 가로등 사이에 몇 개의 길이 있는지 넣기
for i in range(M+1):
    if i == 0:
        road_len.append(spotlights[i])
    elif i == len(spotlights):
        road_len.append(N-spotlights[i-1])
    else:
        road_len.append(spotlights[i]-spotlights[i-1])

# 최소 가로등 길이 구하기
min_height = 0
for j in range(len(road_len)):
    if j == 0:
        min_height = road_len[j]
    elif j == len(road_len)-1:
        min_height = max(min_height, road_len[j])
    else:
        if road_len[j] % 2 == 0:
            x = road_len[j]//2
        else:
            x = road_len[j]//2 + 1
        min_height = max(min_height, x)

print(min_height)