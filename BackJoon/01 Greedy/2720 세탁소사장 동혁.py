'''
2720 세탁소 사장 동혁

큰 수의 법칙..
거스름돈이 모두 5의 배수이기 때문에 그리디로 풀 수 있음 (아니면 DP로 풀어야 함)
'''

import sys
input = sys.stdin.readline

coins = [25, 10, 5, 1]

for t in range(int(input())): # 테스트 케이스만큼 실행
    c = int(input())
    
    for coin in coins:
        print(c // coin, end=' ')
        c %= coin
    print()

