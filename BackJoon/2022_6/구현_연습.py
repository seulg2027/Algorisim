# # 23814번 아 저는 볶음밥이요

# # 볶음밥 먹고 싶다
# # 첫번째 시도 후 다시,,, 생각

# import sys
# input = sys.stdin.readline

# d = int(input())
# n, m, k = map(int, input().split())

# dumpling = (n+m+k)//d
# remain = (n+m+k)%d

# # 조건이 맞을 때까지 옮기는 작업을 반복해줘야함..!
# while (n//d) + (m//d) + (k//d) != dumpling:
#   n_value = n % d
#   m_value = m % d
  
#   if n_value > m_value:
#     n += (d-n_value)
#     k -= (d-n_value)
#   elif n_value < m_value:
#     m += (d-m_value)
#     k -= (d-m_value)
#   else:
#     n += (d-n_value)
#     m += (d-m_value)
#     k -= (d-n_value) + (d-m_value)
# print(k)


# # 1614번 영식이의 손가락

# # 처음엔 dp인줄 알았지만 손가락이 5개밖에없어서 하나하나 다 계산

# import sys
# input = sys.stdin.readline

# n = int(input())
# cnt = int(input())

# first = n-1
# if n == 1 or n == 5:
#   ans = first + 8*cnt
# else: # n이 2,3,4
#   t = cnt // 2
#   r = cnt % 2
#   if n == 2:
#     ans = first + 8*t + 6*r
#   elif n == 3:
#     ans = first + 8*t + 4*r
#   else:
#     ans = first + 8*t + 2*r

# print(ans)


# # 2659번 십자카드 문제

# # 문제를 잘못 이해해서 한참을 헤맴..
# # 시계수를 하나하나 검사해줘야했음

# import sys
# input = sys.stdin.readline

# card = list(input().split())

# def is_clock(card):
#   card += card
#   clock_num = int("".join(card[0:4]))
#   for i in range(1, 4):
#     item = "".join(card[i:i+4])
#     clock_num = min(int(item), clock_num) # 시계수 구하기
#   return clock_num

# clock_num = is_clock(card)

# cnt = 0
# for num in range(1111, clock_num):
#   l = list(str(num))
#   if '0' in l:
#     continue
#   if num == is_clock(l):
#     cnt += 1

# print(cnt+1)


# # 2503 숫자 야구

# # 다시 풀어..!
# # 조건 때문에 오래걸렸다ㅜ 121같이 같은 수가 포함되어있는 것을 고려 안해줘서 헤맸음

# import sys
# input = sys.stdin.readline

# n = int(input())
# candidate = [1 for _ in range(110, 1000)]

# # 111 부터 999까지 수들 중 안되는 수를 제외
# for i in range(110, 1000):
#   if '0' in list(str(i)):
#     candidate[i-110]= 0
#   if len(set(list(str(i)))) < 3:
#     candidate[i-110]= 0

# def numball(number, a, b):
#   list_num = list(str(number))
#   for m in range(110, 1000):
#     if candidate[m-110]:
#       strike = 0
#       ball = 0
#       list_m = list(str(m))
#       set_ball = []
#       for j in range(3):
#         if list_num[j] == list_m[j]:
#           strike += 1
#         elif list_m[j] in list_num and list_m[j] not in set_ball:
#           ball += 1
#           set_ball.append(list_m[j])
#       if strike != a or ball != b:
#         candidate[m-110] = 0

# for _ in range(n):
#   number, a, b = map(int, input().split())
#   candidate[number-110] = 0
  
#   numball(number, a, b)

# print(candidate.count(1))

# # 1789번 수들의 합

# # 너모 쉬움

# import sys
# input = sys.stdin.readline

# s = int(input())
# num = 0

# for i in range(1, sys.maxsize):
#   num += i
#   if s == num:
#     ans = i
#     break
#   elif s < num:
#     ans = i-1
#     break

# print(ans)

# # 1758번 알바생 강호

# import sys
# input = sys.stdin.readline

# n = int(input())
# tips = []
# ans = 0

# for i in range(n):
#   tips.append(int(input()))
# tips.sort(reverse=True)

# for j in range(n):
#   if tips[j] - j > 0:
#     ans += tips[j] - j

# print(ans)

# # 1213번 팰린드롬

# # 정해진거 없음 진짜 구현
# # 반례 모두 고려했으나,, for문 주의해야징

# import sys
# input = sys.stdin.readline

# name = list(input().rstrip())
# alphabet = dict()

# for n in name:
#   if alphabet.get(n) != None:
#     alphabet[n] += 1
#   else:
#     alphabet[n] = 1

# sorted_alphabet = sorted(alphabet.items())
# odd_num = 0
# even_a = ""
# odd_a = ""

# for tu in sorted_alphabet:
#   if tu[1] % 2 == 0: # 짝수일 경우
#     even_a += tu[0] * (tu[1]//2)
#   else: # 홀수일 경우
#     even_a += tu[0] * (tu[1]//2)
#     odd_a += tu[0]
#     odd_num += 1
#     if odd_num > 1:
#       print("I'm Sorry Hansoo")
#       sys.exit(0)

# even_re = list(even_a)
# even_re.reverse()
# even_re = "".join(even_re)

# ans = even_a + odd_a + even_re

# print(ans)