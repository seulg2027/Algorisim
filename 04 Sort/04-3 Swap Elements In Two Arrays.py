# 두 배열의 원소 교체

# 내가 푼 방법
n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 원소를 내림차순으로 정렬하기
A_sorted = sorted(A, reverse=True)
B_sorted = sorted(B, reverse=True)

for i in range(k-1, -1, -1): # k번 바꿀 수 있기 때문에 k-1인덱스까지 확인한다.
  if A_sorted[i] < B_sorted[i]: # 내림차순으로 된 배열에, i번째에서 만약 B의 원소가 크다면
    for j in range(i): # i보다 작은 인덱스의 리스트는 모두 바꿔준다
      A_sorted[j] = B_sorted[j]
    break # 리스트를 바꿔주었다면 즉시 반복문을 빠져나온다 (또 인덱스를 확인해서 여러번 바꾸는 일이 없게 만듦)

result = 0
for item in A_sorted:
  result += item # 리스트 요소의 합을 구한다
print(result)