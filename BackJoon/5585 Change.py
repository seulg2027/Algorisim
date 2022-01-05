# 거스름돈

change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
result = 0

for coin in coins:
  if change // coin > 0:
    s = change // coin
    change %= coin
    result += s

print(result)