# Q09 문자열 압축

# 내가 푼 방법
# 시간 초과.....ㅠ_ㅠ 많이 초과.... 1시간 반 걸려서 했는데 틀림
# 테스트 케이스 5개중 2개 통과
import sys
input = sys.stdin.readline

s = input()
List = [0 for i in range(len(s))]  # s의 길이만큼 초기화(어차피 최대가 1000이니까 상관없을거라 생각)


answer = 0
count = 0  # 각 갯수별로 나온 문자열 갯수
iterate = 1
iterate_str = ''


def solution_one(s):
    global iterate_str
    global iterate
    for i in range(len(s)-1):
        string_1 = s[i]
        string_2 = s[i+1]
        if string_1 == string_2:
            iterate += 1
        else:
            if iterate == 1:
                iterate_str += ''.join(string_1)
            else:
                iterate_str += ''.join(str(iterate) + string_1)
            iterate = 1
    return len(iterate_str)


def solution_multi(x, s):
    global iterate_str
    global iterate
    for i in range(len(s)-x):
        if iterate == 1:
            string_1 = s[i:i+x]
            string_2 = s[i+x:i+x+x]
        else:
            string_1 = s[i:i+x]
            string_2 = s[i*x+1:i*x+1+x]
        if string_1 == string_2:
            iterate += 1
        else:
            if iterate == 1:
                iterate_str += ''.join(string_1[0])
            else:
                iterate_str += ''.join(str(iterate) + string_1)
            if i == len(s)-x-1:
                iterate_str += ''.join(s[len(s)-x:])
            iterate = 1
    return len(iterate_str)-1


def solution(s):
    for x in range(1, len(s)//2):  # 묶음 갯수별로 고려해준다.
        global iterate_str
        global iterate
        global answer
        if x == 1:
            List.insert(1, solution_one(s))
        else:
            List.insert(x, solution_multi(x, s))
        for item in List:
            if item == 0:
                List.remove(0)
        answer = min(List)
    return answer



print(solution(s))


# 답안 예시
# 나랑 생각하는 방향은 같았는데.. 진짜 천재인거같다 어떻게 이런 코드를ㅠㅠㅠㅠㅠㅠ;;;

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1): # 압축 단위 step..
        compressed = ""
        prev = s[0:step] # 0부터 압축한 단위까지
        count = 1
        for j in range(step, len(s), step): # range(start, stop, step)
            if prev == s[j : j+step]: #이렇게 단위를 늘려줄 수 있음..
                count += 1
            else :
                compressed += str(count)+prev if count >= 2 else prev # 만약 반복된 것이면 반복 숫자와 같이 붙여주고, 아니면 문자만
                prev = s[j: j+step] # **여기서 다시 상태를 초기화 시켜준다**
                count = 1
        compressed += str(count)+prev if count >= 2 else prev # 남아있는 문자열에 대해 처리해준다.
        answer = min(answer, len(compressed)) # 오 이런 방법이...
    return answer