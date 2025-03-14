'''
2512번 예산

'''

import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
total = int(input())

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        lower_price = list(filter(lambda x: x<mid, prices))
        need_price = sum(lower_price) + mid * (N-len(lower_price))
        
        if need_price == total:
            return mid
        elif need_price > total:
            end = mid - 1
        elif need_price < total:
            start = mid + 1
    
    if need_price < total:
        return mid
    else:
        return mid-1

print(binary_search(1, max(prices)))