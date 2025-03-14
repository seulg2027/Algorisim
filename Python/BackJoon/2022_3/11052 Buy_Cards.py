# 11052번 카드 구매하기

# # 반례있음 내일 또 풀어봐야함,,,
# # zip 함수 사용

# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# price = list(map(int, input().split()))
# cards = [i for i in range(1, n+1)]
# tmp = []
# for i in range(n):
#     tmp.append(price[i]/cards[i])

# sorted_price = [(i, j) for _,i,j in sorted(zip(tmp, price, cards))]
# q = deque([sorted_price.pop()])
# ans = 0
# while q:
#     cost, card = q.popleft()
#     print(cost, card)
#     num = n // card
#     n -= num * card
#     ans += cost * num
#     if n != 0:
#         q.append(sorted_price.pop())

# print(ans)

# 역시 최대는 크루스칼, 플로이드 아니면 dp,,,

import sys
input = sys.stdin.readline

n = int(input())
price = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j]+price[j], dp[i])

print(dp[n])