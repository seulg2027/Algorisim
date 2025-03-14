# 타겟 넘버

numbers = [1, 1, 1, 1, 1]
target = 3
answer = 0

def Dfs(depth, numbers, total, n, target):
  global answer
  if depth == n:
    if total == target:
      answer += 1
    return
  
  Dfs(depth + 1, numbers, total + numbers[depth], n, target)
  Dfs(depth + 1, numbers, total - numbers[depth], n, target)


def solution(numbers, target):
  global answer
  n = len(numbers)
  Dfs(0, numbers, 0, n, target)
  return answer

print(solution(numbers, target))
