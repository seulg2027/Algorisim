'''
15658번 연산자 끼워넣기(2)

중복가능한 순열을 DFS로 구현
'''

import sys, copy
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
cal_list = ["+", "-", "x", "/"]
cal_num = list(map(int, input().split()))

s = ['' for _ in range(n-1)]

max_value = -sys.maxsize
min_value = sys.maxsize

def calculate(op, res):
    global max_value, min_value
    for i in range(n-1):
        if op[i] == cal_list[0]:
            res[i+1] = res[i] + res[i+1]
        elif op[i] == cal_list[1]:
            res[i+1] = res[i] - res[i+1]
        elif op[i] == cal_list[2]:
            res[i+1] = res[i] * res[i+1]
        elif op[i] == cal_list[3]:
            # 음수이면 양수로 바꾸고 계산하라는 조건
            if res[i] < 0:
                res[i+1] = - (abs(res[i]) // res[i+1])
            else:
                res[i+1] = res[i] // res[i+1]
    max_value = res[-1] if max_value < res[-1] else max_value
    min_value = res[-1] if min_value > res[-1] else min_value

# 최대 4^10, 정해진 4가지 연산자 중 하나씩 고르기
def dfs(x):
    if x == n-1:
        res = copy.deepcopy(a_list)
        calculate(s, res)
        return
    
    for i in range(4):
        if cal_num[i] > 0: # 연산자 개수가 남아있어야 함
            s[x] = cal_list[i]
            cal_num[i] -= 1
            dfs(x+1)
            s[x] = ''
            cal_num[i] += 1

dfs(0)
print(max_value)
print(min_value)