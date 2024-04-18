'''
12904번 가장 긴 팰린드롬

구냥 구현
'''

def solution(s):
    n = len(s)
    max_s = 1 # 가장 짧은 팰린드롬은 1일 수 밖에 없당
    mark = 0
    
    while True:
        ## 지금까지 계산한 가장 긴 팰린드롬보다 첫번째 글자가 더 뒤에 위치하고 있다면
        ## 그냥 종료
        if n - max_s <= mark:
            break
        
        # mark기준으로 팰린드롬인지 확인하기
        for i in range(n-1, mark, -1):
            st = s[mark:i+1]
            re_st = st[::-1] # 파이썬 거꾸로 문자열
            # 팰린드롬 계산하고 반복문 벗어나기
            if re_st == st:
                max_s = max(max_s, i-mark+1)
                break
        
        mark += 1
    
    return max_s