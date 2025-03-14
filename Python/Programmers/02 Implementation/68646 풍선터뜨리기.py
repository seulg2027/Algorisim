'''
68646 풍선 터뜨리기
'''

INF = 1e9

def solution(a):
    answer = len(a)
    n = len(a)
    leftMinValue = [INF] * n
    rightMinValue = [INF] * n
    
    for i in range(n):
        if a[i] < leftMinValue[i]: leftMinValue[i] = a[i] # left 최솟값 갱신
        if i+1 < n : leftMinValue[i+1] = leftMinValue[i]
        if a[n-1-i] < rightMinValue[n-1-i]: rightMinValue[n-1-i] = a[n-1-i] # right 최솟값 갱신
        if n-2-i >= 0 : rightMinValue[n-2-i] = rightMinValue[n-1-i] 
    
    cnt = 0
    for j in range(n):
        if a[j] > leftMinValue[j] and a[j] > rightMinValue[j]: # 값이 두 최솟값보다 클 경우
            cnt += 1
    
    answer -= cnt
    return answer