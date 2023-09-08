'''
입국심사

처음에는 Backtracking을 생각했는데,, 절대 그런 제한 시간이 아니라서 열심히 찾아봄
내 풀이가 아니라 남의 풀이🤨 이해해보려고 노력했당
'''

def solution(n, times):
    answer = 0
    # right = 가장 비효율적인 심사시간
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2 # mid = 심사시간
        com_peo = 0 # mid 시간 내에 심사 완료한 사람
        
        for t in times:
            com_peo += mid // t
            if com_peo >= n:
                break
        # 심사 완료한 사람 >= 심사할 사람
        if com_peo >= n:
            answer = mid
            right = mid - 1
        # 심사 완료한 사람 < 심사할 사람
        else:
            left = mid + 1
    
    return answer