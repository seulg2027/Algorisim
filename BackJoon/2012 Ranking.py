# 등수 매기기


# 처음에 덱을 사용해서 구현했는데
# 덱에 중복값이 안들어가더라.....ㅠㅠㅠ
# 다시 힙을 사용했는데 인덱스 에러 계속 남
# 그냥 이 코드가 잘못된거구나 깨닫고 다시 처음부터 품...
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
rank = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

sorted_rank = [[] for _ in range(N+1)]
sorted_rank[0] = 0 # 초깃값
result = 0
q = []

for person in rank:
  if sorted_rank[person] != []: # 이미 사람이 있다면
    heapq.heappush(q, person) # 큐에 넣는다.
  else: # 사람이 없다면 큐에 넣지 않고 그냥 배치해준다.
    sorted_rank[person] = person

for i in range(1, len(sorted_rank)):
  if sorted_rank[i] == []: # 비어있다면
    rank = heapq.heappop(q) # 한개 꺼냄
    sorted_rank[i] = rank
    result += abs(sorted_rank[i] - i)
  else: # 비어있지 않으면 값이 0이므로 무시
    continue

print(result)

## 다시 푼 코드
# 그냥 수학이었음 ㅠ 좀더 쉽게 생각할걸
import sys

N = int(sys.stdin.readline().rstrip())
rank = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

rank.sort()
result = 0

for index in range(N):
  result += abs(rank[index] - (index + 1))

print(result)