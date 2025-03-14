# Q07 럭키 스트레이트

# 내가 푼 답
# 백준 사이트 - 맞았음
N = input()
critial = int(len(N)/2)

left = N[0:critial]
right = N[critial:len(N)]
left_result = 0
right_result = 0

for i in range(critial):
    left_result += int(left[i])
    right_result += int(right[i])

if left_result == right_result:
    print("LUCKY")
else:
    print("READY")
