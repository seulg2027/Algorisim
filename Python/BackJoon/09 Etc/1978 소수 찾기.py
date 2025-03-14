'''
1978번 소수 찾기
에라토스테네스의 체
'''
import sys, math
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
cnt = 0 # 소수 개수
m = 1000 # 1000개 이하의 자연수에 대해 소수 판별
arr = [True for _ in range(m+1)]
arr[0], arr[1] = False, False

for i in range(2, int(math.sqrt(m))+1):
    if arr[i] == True:
        j = 2
        while i * j <= m:
            arr[i*j] = False
            j += 1

for num in numbers:
    if arr[num]:
        cnt += 1

print(cnt)