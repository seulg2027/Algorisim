'''
24416번 알고리즘 수업 - 피보나치 수 1
재귀함수와 동적계획법의 시간복잡도를 비교할수 있는 문제..
'''

import sys
input = sys.stdin.readline

fib_cnt = 1
fibona_cnt = 0

def fib(n):
    global fib_cnt
    if n == 1 or n == 2:
        return 1
    else:
        fib_cnt += 1
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    global fibona_cnt
    for i in range(3, n+1):
        fibona_cnt += 1
        dp[i] = dp[i-1] + dp[i-2]

n = int(input())

fib(n)
fibonacci(n)

print(fib_cnt, fibona_cnt)