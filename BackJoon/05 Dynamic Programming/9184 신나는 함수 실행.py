'''
9184번 신나는 함수 실행

대놓고 DP
'''

import sys
input = sys.stdin.readline

def w(a, b, c):
    dp = list(list([1] * (21) for _ in range(21)) for _ in range(21))
    # 한 원소라도 0보다 작으면 1 리턴, 20보다 크면 w(20, 20, 20) 리턴
    # return을 안쓰고 w(a, b, c) 실행하면 밑의 for문이 모두 계속 실행되므로 주의.
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    # 20까지만 계산하면 되므로
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if i < j < k:
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1 :
        break
    
    res = w(a, b, c)
    
    print(f"w({a}, {b}, {c}) = {res}")
