/**
 * 바깥쪽 -> 안쪽으로 전류 침투
 */
import java.io.*;
import java.util.*;

public class boj_침투 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int[][] graph = new int[m][n];
        for (var i=0; i<m; i++) {
            graph[i] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        }
        boolean[][] visited = new boolean[m][n];

        Queue<int[]> q = new LinkedList<>();
        for (var i=0; i<n; i++) {
            if (graph[0][i] == 0){
                q.offer(new int[]{0, i});
                visited[0][i] = true;
            }
        }

        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int maxRow = 1;

        while (!q.isEmpty()) {
            int[] now = q.poll();

            for (var i=0; i<4; i++) {
                int nx = dx[i] + now[0];
                int ny = dy[i] + now[1];
                if (0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny]) {
                    if (graph[nx][ny] == 0) {
                        q.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                        maxRow = Math.max(maxRow, nx+1);
                    }
                }
            }
        }

        if (maxRow == m) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
