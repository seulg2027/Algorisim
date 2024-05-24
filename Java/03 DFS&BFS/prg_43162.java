import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class prg_43162 {
    static boolean[] visited;
    static int answer = 0;
    
    public int solution(int n, int[][] computers) {
        List<Integer>[] graph = new ArrayList[5];
        visited = new boolean[n];
        
        for (int i=0; i<n; i++) {
            graph[i] = new ArrayList<Integer>();
            for (int j=0; j<n; j++) {
                if (i != j && computers[i][j] == 1) {
                    graph[i].add(j);
                }
            }
        }
        
        for (int j=0; j<n; j++) {
            if (!visited[j]) {
                bfs(j, graph);
                answer ++;
            }
        }
        return answer;
    }
    
    public static void bfs(int x, List<Integer>[] graph) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(x);
        visited[x] = true;
        while (!queue.isEmpty()) { // 큐가 비었다면
            int a = queue.poll();
            for (int com : graph[a]) {
                if (!visited[com]) {
                    visited[com] = true;
                    queue.add(com);
                }
            }
        }
    }
}
