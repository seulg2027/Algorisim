# Q19. 연산자 끼워넣기
# ..??? 답 예시 돌렸는데 테케 틀림;

# 내가 푼 방법,, 테케 하나 통과
# 연산을 조합으로 경우의 수를 만들까 고민하다가 재귀호출을 사용해보았는데 실패
import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

visited = [False] * n
result = a[0]
max_re = -1e9
min_re = 1e9

def calculate(now, result):
  global add, sub, mul, div, n, max_re, min_re
  visited[now] = True # 현재 가지고있는 숫자는 방문
  if visited[n-1] == True:
    max_re = max(max_re, result)
    min_re = min(min_re,result)
  else:
    if add > 0:
      add -= 1
      result += a[now+1]
      calculate(now+1, result)
    if sub > 0:
      sub -= 1
      result -= a[now+1]
      calculate(now+1, result)
    if mul > 0:
      sub -= 1
      result *= a[now+1]
      calculate(now+1, result)
    if div > 0:
      div -= 1
      result //= a[now+1]
      calculate(now+1, result)

calculate(0, result)
print(max_re, min_re)


## 답 예시
n = int(input())

data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

# 깊이 우선 탐색 메소드
def dfs(i, now):
  global min_value, max_value, add, sub, mul, div
  # 모든 연산자 사용 시 최솟값, 최댓값 업데이트
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    ## 에엥... 나랑 똑같이 한거같은데...왜 결과값이 다르지ㅠ
    if add > 0:
      add -= 1
      dfs( i+1, now + data[i] ) # 현재 있는 데이터랑 합친다.
      add += 1 # 여기가 다름! 연산자 갯수를 다시 원상 복귀 시켜줘야한다.
    if sub > 0:
      sub -= 1
      dfs( i+1, now - data[i] ) 
      sub += 1
    if mul > 0:
      sub -= 1
      dfs( i+1, now * data[i] ) 
      sub += 1
    if div > 0:
      div -= 1
      dfs( i+1, int(now / data[i]))
      div += 1

dfs(1, data[0])
print(max_value)
print(min_value)