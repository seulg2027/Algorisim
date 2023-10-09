'''
16139번 인간-컴퓨터 상호작용
'''

# 50점 풀이, dict 사용
# copy하는데 연산이 오래 걸린 듯..
import sys, copy
input = sys.stdin.readline

s = input().strip()
sum_list = [dict() for _ in range(len(s))]

for i in range(len(s)): # 200,000 번 이하로 실행
    if i > 0:
        sum_list[i] = copy.deepcopy(sum_list[i-1])
    if s[i] in sum_list[i].keys():
        sum_list[i][s[i]] += 1
    else:
        sum_list[i][s[i]] = 1

for _ in range(int(input())):
    alphabet, start, end = input().split()
    end_sum = sum_list[int(end)][alphabet] if alphabet in sum_list[int(end)].keys() else 0
    if int(start) == 0:
        start_sum = 0
    else:
        start_sum = sum_list[int(start)-1][alphabet] if alphabet in sum_list[int(start)-1].keys() else 0
    print(end_sum - start_sum)


# 100점 풀이, 2차원 배열로 사용
# 50점 풀이와 아이디어는 비슷
import sys
input = sys.stdin.readline

s = input().strip()
sum_list = [[0 for _ in range(26)] for _ in range(len(s))]
sum_list[0][ord(s[0]) - 97] = 1

for i in range(1, len(s)):
    sum_list[i][ord(s[i]) - 97] += 1
    for j in range(26):
        sum_list[i][j] += sum_list[i-1][j]

for i in range(int(input())):
    alphabet, start, end = input().split()
    if int(start) > 0:
        res = sum_list[int(end)][ord(alphabet)-97] - sum_list[int(start)-1][ord(alphabet)-97]
    else:
        res = sum_list[int(end)][ord(alphabet)-97]
    print(res)