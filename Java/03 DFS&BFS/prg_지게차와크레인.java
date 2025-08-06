/**
지게차 : 알파벳 1개
크레인 : 알파벳 2개
*/
import java.util.*;

public class prg_지게차와크레인 {
    class Solution {
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int n, m;
        
        public int solution(String[] storage, String[] requests) {
            int answer = 0;
            n = storage.length;
            m = storage[0].length();
            Set set = new HashSet<>();
            
            int[][] graph = new int[n + 2][m + 2];
            for (var i = 1; i < n + 1; i++) {
                for (var j = 1; j < m + 1; j++) {
                    graph[i][j] = 1;
                }
            }
            
            for (String req : requests) {
                int size = req.length();
                char r = req.charAt(0);
                
                // 지게차
                if (size == 1) {
                    tryForkLift(graph, storage, r);
                // 크레인
                } else if (size == 2 && !set.contains(r)) {
                    tryForkRain(graph, storage, r);
                    set.add(r);
                }
            }
            
            for (var i = 1; i < n + 1; i++) {
                for (var j = 1; j < m + 1; j++) {
                    if (graph[i][j] == 1) answer++;
                }
            }
            
            return answer;
        }
        
        private int[][] tryForkLift(int[][] graphs, String[] storage, char a) {
            Queue<int[]> queue = new LinkedList<>();
            queue.offer(new int[]{0, 0});
            boolean[][] visited = new boolean[n + 2][m + 2];
            
            while (!queue.isEmpty()) {
                int[] now = queue.poll();
                for (int i = 0; i < 4; i++) {
                    int nx = now[0] + dx[i];
                    int ny = now[1] + dy[i];
                    if (0 <= nx && nx < n + 2 && 0 <= ny && ny < m + 2 && !visited[nx][ny]) {
                        if (graphs[nx][ny] == 0) {
                            queue.offer(new int[]{nx, ny});
                        } else if (storage[nx - 1].charAt(ny - 1) == a) {
                            graphs[nx][ny] = 0; // 물류창고에서 꺼내기
                        }
                        visited[nx][ny] = true;
                    }
                }
            }
            
            return graphs;
        }
        
        private int[][] tryForkRain(int[][] graphs, String[] storage, char a) {
            for (int s = 0; s < storage.length; s++) {
                int len = storage[s].length();
                for (int i = 0; i < len; i++) {
                    if (storage[s].charAt(i) == a) {
                        graphs[s + 1][i + 1] = 0; // 물류 창고에서 꺼내기
                    }
                }
            }
            return graphs;
        }
    }
}
