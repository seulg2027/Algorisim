## 튜플

## 통과

import re
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

def solution(s):
  answer = []
  set_list = []
  for i in s.split('},{'):
    set_list.append([])
    if ('{{' in i):
      i = re.sub("{", "", i)
    if ('}}' in i):
      i = re.sub("}", "", i)
    for j in i.split(','):
      set_list[len(set_list)-1].append(int(j))
  cnt = 1
  num = set()
  while len(answer) != len(set_list):
    for h in range(len(set_list)):
      if (len(set_list[h]) == cnt): # 개수가 딱 맞으면
        cnt += 1
        result = [i for i in set_list[h] if i not in num]
        answer.append(result.pop())
        num.update(set_list[h])
  return answer

solution(s)
