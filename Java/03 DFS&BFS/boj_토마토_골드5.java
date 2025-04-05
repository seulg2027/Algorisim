/**
 * 문제 풀이 : BFS
 * 1. 익은 토마토 자리 표시하기
 * 2. 익은 토마토 주변으로 확산
 * 3. 마지막으로 토마토 익었는지 확인
 */
import java.io.*;
import java.util.*;

public class boj_토마토_골드5 {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] boxes = new int[m][n];

        boolean[][] visited = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<>();

        for (var i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            for (var j = 0; j < n; j++) {
                boxes[i][j] = Integer.parseInt(st.nextToken());
                if (boxes[i][j] == 1) {
                    queue.offer(new int[]{i, j, 0});
                    visited[i][j] = true;
                }
            }
        }

        int time = 0;
        
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            time = Math.max(now[2], time);

            for (var i = 0; i < 4; i++) {
                int nx = dx[i] + now[0];
                int ny = dy[i] + now[1];
                if (0 <= nx && nx < m && 0 <= ny && ny < n && boxes[nx][ny] != -1 && !visited[nx][ny]) {
                    boxes[nx][ny] = 1;
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny, now[2] + 1});
                }
            }
        }

        // 토마토가 다 익었는지 확인
        boolean isTrue = true;
        for (var i = 0; i < m; i++) {
            for (var j = 0; j < n; j++) {
                if (boxes[i][j] == 0) isTrue = false;
            }
        }

        if (isTrue) bw.write(String.valueOf(time) + "\n");
        else bw.write(String.valueOf(-1) + "\n");

        bw.flush();
        bw.close();
    }
}
