# 2110번 공유기 설치

# # 백트래킹으로 품(조합,,,) => 시간초과

# import sys
# input = sys.stdin.readline

# n, c = map(int, input().split())
# home = []
# for _ in range(n):
#   home.append(int(input()))

# home.sort()
# router = [0] * c
# ans = []

# def make_cnt(x):
#   if x == c:
#     cnt = sys.maxsize
#     for i in range(c-1):
#       cnt = min(router[i+1]-router[i], cnt)
#     ans.append(cnt)
#   else:
#     for i in range(n):
#       if max(router) < home[i]:
#         router[x] = home[i]
#         make_cnt(x+1)
#         router[x] = 0

# make_cnt(0)
# print(max(ans))

# 정답 코드
# 이분 탐색,,,

n, c = map(int, input().split())

array = []
for i in range(n):
  array.append(int(input()))

array.sort()


def binary_search(array, start, end):
  while start <= end:
    mid = (start + end) // 2
    current = array[0]
    count = 1

    for i in range(1, len(array)):
      if array[i] >= current + mid:
        count += 1
        current = array[i]

    if count >= c:
      global answer
      start = mid + 1
      answer = mid
    else:
      end = mid - 1


start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)