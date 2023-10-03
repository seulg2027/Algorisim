'''
2869 달팽이는 올라가고 싶다
'''

import sys, math
input = sys.stdin.readline

A, B, V = map(int, input().split())
D = math.ceil((V-A)/(A-B)+1)

print(D)