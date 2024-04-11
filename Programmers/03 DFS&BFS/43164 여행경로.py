'''
내가 푼 답 -> 75점
'''

import copy
result = []

def dfs(i, tickets, route, used):
    global result
    if 1 not in used:
        if len(route) == len(tickets)+1 and result == []:
            result = copy.deepcopy(route)
            return
    else:
        for j in range(len(tickets)):
            if tickets[i][1] == tickets[j][0] and used[j] == 1:
                route.append(tickets[j][1])
                used[j] -= 1
                dfs(j, tickets, route, used)
                route.pop(-1)
                used[j] += 1
                return
    return

def solution(tickets):
    n = len(tickets)
    answer = []
    
    tickets.sort(key = lambda x: (x[1], x[0]))
    
    used = [1 for _ in range(n)]
    for i in range(n):
        if tickets[i][0] == "ICN":
            used[i] -= 1
            dfs(i, tickets, ["ICN", tickets[i][1]], used)
            used[i] += 1
    
    return result


'''
정답.
'''

def solution(tickets):
    answer = []
    tickets.sort(key = lambda x: (x[0], x[1]))
    
    # DFS
    def getPath(t, path):
        if len(t) == 0:
            return path
        
        now = path[-1]
        valid_idx = -1
        
        for i in range(len(t)):
            if t[i][0] == now:
                valid_idx = i
                break
        
        if valid_idx == -1:
            return []
        
        while t[valid_idx][0] == now:
            nxt_path = getPath(t[:valid_idx] + t[valid_idx + 1:], path + [t[valid_idx][1]])
            
            if nxt_path != []:
                return nxt_path
            
            valid_idx += 1
        
        return []
    
    return getPath(tickets, ["ICN"])