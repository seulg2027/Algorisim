/**
N 세로 격자의 수, M 가로 격자의 수
얼음 외부 공기 -1
얼음 1
얼음 내부 공간 0
1. 얼음 외부 공간 구하기
2. 얼음 중 외부 공기와 2칸 이상 맞닿아있는 구역 표시하기 (다른 그래프에 표시하기)
3. 얼음 없애기
*/
import java.io.*;
import java.util.*;

public class softeer_동계테스트시점예측 {
    public class Main {
        static int[] dx = {0, 1, 0, -1};
        static int[] dy = {1, 0, -1, 0};
        static int[][] iceMap;
        static int n, m;
    
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            iceMap = new int[n][m];
    
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < m; j++) {
                    iceMap[i][j] = Integer.parseInt(st.nextToken());
                }
            }
    
            markOuterAir();  // BFS로 외부 공기(-1) 설정
            int answer = 0;
    
            while (meltIce()) { // 얼음이 녹을 수 있으면 반복
                answer++;
                markOuterAir();
            }
    
            bw.write(String.valueOf(answer));
            bw.flush();
            bw.close();
        }
    
        private static void markOuterAir() {
            Queue<int[]> q = new LinkedList<>();
            boolean[][] visited = new boolean[n][m];
            q.offer(new int[]{0, 0});
            iceMap[0][0] = -1;
            visited[0][0] = true;
            
            while (!q.isEmpty()) {
                int[] now = q.poll();
                int cx = now[0], cy = now[1];
    
                for (int i = 0; i < 4; i++) {
                    int nx = cx + dx[i];
                    int ny = cy + dy[i];
    
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && (iceMap[nx][ny] == 0 || iceMap[nx][ny] == -1)) {
                        q.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                        iceMap[nx][ny] = -1;
                    }
                }
            }
        }
    
        private static boolean meltIce() {
            boolean isMelting = false;
            List<int[]> meltList = new ArrayList<>();
    
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (iceMap[i][j] == 1) {
                        int cnt = 0;
                        for (int k = 0; k < 4; k++) {
                            int nx = i + dx[k];
                            int ny = j + dy[k];
                            if (nx >= 0 && nx < n && ny >= 0 && ny < m && iceMap[nx][ny] == -1) {
                                cnt++;
                            }
                        }
                        if (cnt >= 2) {
                            meltList.add(new int[]{i, j});
                            isMelting = true;
                        }
                    }
                }
            }
    
            for (int[] ice : meltList) {
                iceMap[ice[0]][ice[1]] = -1;
            }
    
            return isMelting;
        }
    }
}
