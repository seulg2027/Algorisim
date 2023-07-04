'''
18870번 좌표 압축
'''

import sys
input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))
sorted_num_list = sorted(list(set(num_list)))

dic_list = {sorted_num_list[i]: i for i in range(len(sorted_num_list))}

for m in num_list:
    print(dic_list[m], end=' ')