'''
72411번 메뉴 매뉴얼
'''

def solution(orders, course):
    answer = []
    
    # DFS 메서드 실행
    def dfs(cnt, start):
        if cnt == c:
            s = "".join(sorted(menu))
            counter[s] = 1 if counter.get(s) == None else counter[s] + 1
            return
        
        # 단품 메뉴 구성하기
        for i in range(start, len(order)):
            menu[cnt] = order[i]
            dfs(cnt+1, i+1)
    
    for c in course:
        menu = [0 for _ in range(c)]
        counter = dict()
        for order in orders:
            dfs(0, 0)
        # 메뉴 코스요리 주문 횟수에 따라 내림차순으로 정렬하기
        sort_counter = sorted(counter.items(), key=lambda x:-x[1])
        
        for i in range(len(sort_counter)):
            if (i == 0 and sort_counter[i][1] > 1) or (sort_counter[i][1] == sort_counter[0][1] and sort_counter[i][1] > 1):
                answer.append(sort_counter[i][0])
            else:
                break
    
    answer.sort()
    
    return answer