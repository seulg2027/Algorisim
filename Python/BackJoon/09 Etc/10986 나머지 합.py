'''
10986번 나머지 합
'''

# 시간 초과 코드 - 100점 코드는 내일..
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
sum_num = list(0 for _ in range(n+1))
sum_num[1] = numbers[0]
cnt = 0

for i in range(1, n+1):
    sum_num[i] = sum_num[i-1] + numbers[i]

for j in range(n+1):
    for k in range(1, n-j+1):
        res = sum_num[j+k] - sum_num[j]
        if res % m == 0:
            cnt += 1

print(cnt)