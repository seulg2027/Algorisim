# k번째 수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
  answer = []
  for cm in commands:
    i, j, k = cm
    lists = array[i-1:j]
    lists.sort()
    answer.append(lists[k-1])
  return answer

print(solution(array, commands))