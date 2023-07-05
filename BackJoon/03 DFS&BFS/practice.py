'''
백트래킹 연습
'''

n, k = map(int, input().split())

jump = []
cnt = 0

def backtracking(s):
    global cnt
    if len(jump) == k and sum(jump) == n:
        cnt += 1
        return
    
    for i in range(s, n+1):
        jump.append(i)
        backtracking(i+1)
        jump.pop()

backtracking(1)
print(cnt)