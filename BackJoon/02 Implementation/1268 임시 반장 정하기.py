'''
1268번 임시 반장 정하기

'''

import sys
input = sys.stdin.readline

N = int(input())
mate = list(list(map(int, input().split())) for _ in range(N))
res = list(set() for _ in range(N))

# N이 최대 1000 이므로 최대 1000 * 999 로 상관 없음
for j in range(5):
    for i in range(N):
        for k in range(i+1, N):
            if mate[i][j] == mate[k][j]:
                res[i].add(k+1)
                res[k].add(i+1)

max_value = -1 # 아무도 같은 반이 된 적이 없다면 1번 출력해야 함
max_student = 0
for r in range(N):
    if max_value < len(res[r]):
        max_value = len(res[r])
        max_student = r+1

print(max_student)