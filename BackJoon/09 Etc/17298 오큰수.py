"""
17298번 오큰수

다른 사람들 풀이랑 다르게 뒤에서부터 스택에 넣었다
암튼 맞았어용ㅎㅎ
"""

import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

# 가장 마지막 스택은 정해져있음
stack = [a[-1]]
answer = [-1]

# 뒤부터 시작
for i in range(N - 2, -1, -1):
    # 만약 바로 앞의 수가 더 크면 바로 집어넣기
    if a[i] < a[i + 1]:
        answer.append(a[i + 1])
        stack.append(a[i + 1])
    # 아니라면 스택으로 검사하기
    else:
        is_push = False
        while stack:
            # 가장 오른쪽에 가까운 수에서 오큰수가 나오면 answer에 집어넣기
            if stack[-1] > a[i]:
                now = stack.pop()
                answer.append(now)
                stack.append(now)
                is_push = True
                break
            # 아니라면 스택에서 빼주기(현재 수가 더 크므로)
            else:
                stack.pop()
        if not is_push:
            answer.append(-1)

answer.reverse()

print(*answer)


"""
다른 사람들 풀이
"""

import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)
