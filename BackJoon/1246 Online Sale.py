# 온라인 판매

n, m = map(int, input().split())

price = [int(input()) for _ in range(m)]
sorted_price = sorted(price, reverse=True)
result = 0

for i in range(m):
  if i+1 <= n:
    calculate = sorted_price[i] * (i+1)
  else:
    calculate = sorted_price[i] * n
  if result <= calculate:
    result = calculate
    max_price = sorted_price[i]

print(max_price, result)