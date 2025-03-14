'''
214291 집합과 쿼리
정확도는 다 맞는 것 같은데,, 시간을 통과하는 게 만만치 않다ㅠㅠ
'''

cnt = 0

def query1(q, x, y):
    update_q = []
    set_y = {}
    set_x = {}
    for j in q:
        if y in j:
            if x in j: # y집합에 x가 있는 경우,, 그냥 넣는다.
                update_q.append(j)
            set_y = j # y집합에 x가 없다면
        elif x in j:
            set_x = j # x집합에 y가 없다면
        else: update_q.append(j)
    if (set_y):
        set_y = dict((key, cnt) for key in list(set_y.keys()))
        set_x.update(set_y)
    update_q.append(set_x)
    return update_q

def query2(q, x, y):
    update_q = []
    new_set = {}
    add_set = {}
    for j in q:
        keys = list(j.keys())
        if x in keys: # x가 있는 집합 탐색
            idx_x = keys.index(x)
            idx_y = keys.index(y)
            if idx_x < idx_y: # y가 들어온 시간이 x보다 더 늦었을 경우만
                new_set = dict((a, cnt) for a in keys[idx_x: idx_y+1])
                add_set = dict((a, j[a]) for a in keys[:idx_x] + keys[idx_y+1:])
            else:
                add_set = j
        else:
            update_q.append(j)
    update_q.append(new_set)
    update_q.append(add_set)
    return update_q

def query3(q, x, y):
    for j in q:
        if y in j:
            if x in j:
                return "Yes"
            return "No"

def solution(n, queries):
    global cnt
    answer = []
    querySet = [{i : 0} for i in range(n)]
    
    for ex in queries:
        cnt += 1
        if ex[0] == 1:
            querySet = query1(querySet, ex[1], ex[2])
        elif ex[0] == 2:
            querySet = query2(querySet, ex[1], ex[2])
        else:
            answer.append(query3(querySet, ex[1], ex[2]))
    
    return answer