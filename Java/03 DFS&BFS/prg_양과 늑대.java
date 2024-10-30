/**
* 방문했던 노드를 다시 방문할 수 있음
=> DFS
*/
import java.util.*;

class Solution {
    int answer = 0;
    Set<Integer> visited = new HashSet<>();
    
    public int solution(int[] info, int[][] edges) {
        visited.add(0);
        dfs(0, 1, edges, info);
        return answer;
    }
    
    private void dfs(int wolf, int sheep, int[][] edges, int[] info) {
        if (wolf >= sheep) return;
        
        answer = Math.max(answer, sheep);
        
        for (int[] edge : edges) {
            int parent = edge[0], child = edge[1]; // 부모, 자식
            if (visited.contains(parent) && !visited.contains(child)) {
                visited.add(child);
                
                if (info[child] == 0) { // 양
                    dfs(wolf, sheep + 1, edges, info);
                } else {
                    dfs(wolf + 1, sheep, edges, info);
                }
                
                visited.remove(child);
            }
        }
    }
}