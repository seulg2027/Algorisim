# 가장 큰 수

numbers = [ 979, 97, 978, 81,818,817]

def Key(data):
  list_num = ''
  if len(str(data)) == 1:
    list_num += str(data)[0] * 3
    list_num += '0'
    return list_num
  elif len(str(data)) == 2:
    list_num += str(data)[0]
    list_num += str(data)[1] * 2
    list_num += '1'
    return list_num
  elif len(str(data)) == 3:
    list_num += str(data)[0]
    list_num += str(data)[1]
    list_num += str(data)[2]
    list_num += '2'
    return list_num
  else:
    return "1000"

def solution(numbers):
  answer = ''
  sort_num = sorted(numbers, key=Key, reverse=True)
  print(sort_num)
  for s in sort_num:
    answer += str(s)
  if int(answer) == 0:
    answer = "0"
  return answer

print(solution(numbers))