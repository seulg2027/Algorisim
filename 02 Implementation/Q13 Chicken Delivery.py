# Q13 치킨 배달

# 내가 푼 방법
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

chicken, home = [], []

for i in range(n):
  city_map = list(map(int, input().split()))
  for j in range(n):
    if city_map[j] == 1: # 집
      home.append([i, j])
    elif city_map[j] == 2: # 치킨
      chicken.append([i, j])

home_com = list(combinations(home, m))
result = []

for comb in home_com:
  print(comb)
  for data in comb:
    x = data[0]
    y = data[1]
    distance = 2*n
    for location in chicken:
      c_x = location[0]
      c_y = location[1]
      distance = min(distance, abs(c_x - x) + abs(c_y - y))
    result[comb.index(data)] += distance

city_chicken_distance = min(result)
print(city_chicken_distance)