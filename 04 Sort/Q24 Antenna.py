# 안테나

# 내가 푼 방법
# 반복문을 덜 돌게 하려고 했음
# 하지만 pypy로 돌렸을때도 시간초과......ㅜ
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

critical = 0
data.sort() # 데이터 오름차순 정렬
middle = (data[n-1] // 2 if data[n-1] % 2 == 0 else data[n-1] // 2 + 1) # 위치의 중간값을 구한다.
for i in range(len(data)):
  critical += data[i]
critical //= n # 데이터의 중간값을 구한다.

result = 1e9
compare = 1e9
antenna = 0

if middle > critical:
  for i in range(1, critical): # 1~데이터의 중간 지점까지
    for j in range(n):
      compare += abs(data[j] - i)
    if result > compare: # result값이 클 때만 실행 (같을 때는 처리가 안되므로 값이 같을 때, 예외 처리 가능)
      result = compare
      antenna = i
elif middle < critical:
  for i in range(critical, data[n-1]):
    for j in range(n):
      compare += abs(data[j] - i)
    if result > compare:
      result = compare
      antenna = i
elif middle == critical:
  antenna = critical

print(antenna)

###################################   답안 예시    ###################################
# 이거 보고 울뻔함......

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1) // 2])