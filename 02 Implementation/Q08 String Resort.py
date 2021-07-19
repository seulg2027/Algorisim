# Q08 문자열 재정렬
# 리스트 => 문자열로 변환할 때 "".join() 형태로 많이 쓰인다.

# 내가 푼 답
data = input()
integer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
plus = 0

for i in range(len(data)):
    for j in range(len(integer)):
        if data[i] == integer[j]:
            plus += int(data[i])
            data = data.replace(data[i], "")
            break
    if i == len(data):
        break


string = "".join(sorted(list(data)))

print((plus != 0) if (string + str(plus)) else string)


# 답안 예시
data = input()
result = []
value = 0

for x in data:
    # isalpha() 함수를 사용
    if x.isalpha():  # 문자라면 result에 삽입
        result.append(x)
    else:  # 숫자는 다른 변수에 따로 더하기..
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))  # 리스트를 문자열로 변환하여 마지막에 출력
