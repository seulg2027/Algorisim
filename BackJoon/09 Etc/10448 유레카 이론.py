'''
10448번 유레카 이론
'''

import sys
input = sys.stdin.readline

T = int(input())

t_list = []
for n in range(1, 44):
    t_list.append(int(n*(n+1)/2))

for _ in range(T):
    num = int(input())
    
    # 주어진 수보다 작은 수들만 따로 리스트 만듦
    c_list = list(x for x in t_list if x < num)
    is_True = False
    
    # 그 수들 중에서 3개로 표현할 수 있는지 검사
    # O(N) = 44 * 44 * 44 
    for i in range(len(c_list)):
        for j in range(i, len(c_list)):
            for k in range(j, len(c_list)):
                if c_list[i] + c_list[j] + c_list[k] == num:
                    is_True = True
    
    print(1) if is_True == True else print(0)

