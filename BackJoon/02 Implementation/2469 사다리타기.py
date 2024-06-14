'''
2469번 사다리타기

* 문자열은 자바처럼 변경 불가능 -> 배열로 만들어서 변경할 것

3 <= k <= 26, 3 <= n <= 1000

[내 풀이]
구해야하는 사다리 기준으로 생각
 -> 사다리를 타고 내려오는 처음 문자열, 사다리를 타고 올라가는 최종 문자열을 비교하면 되겠다고 생각
 -> 비교할 때 다르면 - 다리 놓고, 문자 변경
 -> 같으면 * 넣음
최종으로 문자열 변경한 것 비교해서 같으면 사다리 제대로 생성, 아니면 x넣기
'''

import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
f_seq = list(chr(i) for i in range(65, 65+k)) # 처음 참가자 순서
l_seq = list(input().rstrip()) # 마지막 참가자 순서
ladder = list(input().rstrip() for _ in range(n))

def swap_seq(seq, n_ladder):
    for j in range(k-1):
        if n_ladder[j] == '*':
            continue
        tmp = seq[j]
        seq[j] = seq[j+1]
        seq[j+1] = tmp

# 처음 사다리 타고 내려가면
for i in range(n):
    now_ladder = ladder[i]
    if now_ladder[0] == '?':
        break
    swap_seq(f_seq, now_ladder)

# 아래 사다리 타고 올라가면
for i in range(n-1, 0, -1):
    now_ladder = ladder[i]
    if now_ladder[0] == '?':
        break
    swap_seq(l_seq, now_ladder)

ans = []

# 비교한 뒤 사다리 만들기
for j in range(k-1):
    if f_seq[j] != l_seq[j]:
        ans.append('-')
        tmp = f_seq[j]
        f_seq[j] = f_seq[j+1]
        f_seq[j+1] = tmp
    else:
        ans.append('*')

if f_seq != l_seq:
    ans = ['x' for _ in range(k-1)]

print(''.join(ans))
