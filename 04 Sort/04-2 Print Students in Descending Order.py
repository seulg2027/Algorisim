# 성적이 낮은 순서로 학생 출력하기

# 내가 푼 방법
n = int(input())
array = []

for i in range(n):
  array.append(input().split())

def Key(data):
  return data[1]

students = sorted(array, key=Key)

for student in students:
  print(student[0], end=' ')
