'''
20920번. 영단어 암기는 괴로워

Counter(list())
 => dictionary 로 사용하기, items(), keys(), values() 잊지 말기.

'''

import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
alphabets = dict(Counter(list(input().rstrip() for _ in range(n))))

result = sorted(alphabets.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

for a, b in result:
    if len(a) >= m:
        print(a)

