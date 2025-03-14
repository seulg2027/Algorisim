# CH05 - 볼링볼 고르기

# 내가 푼 방법
from itertools import combinations
from collections import Counter
N, M = map(int, input().split())
K = list(map(str, input().split()))

com = list(combinations(K, 2))
minus = 0
result = 0

for i in range(1, M+1):
    string = str(i)
    counter = Counter(K)
    num = counter[string]
    minus += num - 1
    num = 0

result = len(com) - minus

print(result)

# 답안 예시
n, m = map(int, input().split())
data = list(map(str, input().split()))

array = [0] * 11  # 0에서 10까지의 무게를 담을 수 있는 리스트

for x in data:
    array[x] += 1  # 중복된 볼링공의 개수를 리스트로 담는다
result = 0

for i in range(1, m+1):
    n -= array[i]  # 중복되는 볼링공 개수를 제거
    result += array[i]  # 두번째 선택하는 경우의 수와 곱하기
print(result)
