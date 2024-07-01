/**
 * 5427번 불
 * BFS
 */

import java.io.*;
import java.util.*;

public class boj_5427 {
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int test = Integer.parseInt(br.readLine());

        while (test-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            char[][] buildingMap = new char[n][m];

            Queue<int[]> fireDest = new LinkedList<>();
            int[] startSanggun = new int[2];

            for (int i = 0; i < n; i++) {
                String line = br.readLine();
                for (int j = 0; j < m; j++) {
                    buildingMap[i][j] = line.charAt(j);
                    if (buildingMap[i][j] == '@') {
                        startSanggun[0] = i;
                        startSanggun[1] = j;
                    } else if (buildingMap[i][j] == '*') {
                        fireDest.add(new int[]{i, j});
                    }
                }
            }

            int[] result = exitBuilding(buildingMap, n, m, fireDest, startSanggun);
            
            if (result[1] == 1) {
                bw.write(String.valueOf(result[0]) + "\n");
            } else {
                bw.write("IMPOSSIBLE\n");
            }
            bw.flush();
        }

        bw.close();
    }

    private static int[] exitBuilding(char[][] buildingMap, int n, int m, Queue<int[]> fireDest, int[] startSanggun) {
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];

        q.add(new int[]{startSanggun[0], startSanggun[1], 0});
        visited[startSanggun[0]][startSanggun[1]] = true;
        int time = -1; // 먼저 확산 후, 움직임
        int cnt = 0;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int x = now[0];
            int y = now[1];
            cnt = now[2];

            if (0 > x || x >= n || 0 > y || y >= m) {
                return new int[]{cnt, 1};
            }

            if (time != cnt) {
                // fire 확산
                int size = fireDest.size();
                for (int i = 0; i < size; i++) {
                    int[] fire = fireDest.poll();
                    for (int k = 0; k < 4; k++) {
                        int nx = fire[0] + dx[k];
                        int ny = fire[1] + dy[k];
                        if (0 <= nx && nx < n && 0 <= ny && ny < m && (buildingMap[nx][ny] == '.' || buildingMap[nx][ny] == '@')) {
                            buildingMap[nx][ny] = '*';
                            fireDest.add(new int[]{nx, ny});
                        }
                    }
                }
                time = cnt;
            }

            // 빌딩 탈출
            for (int i = 0; i < 4; i ++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (buildingMap[nx][ny] == '.' && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny, cnt+1});
                    }
                } else {
                    q.add(new int[]{nx, ny, cnt+1});
                }
            }
        }

        return new int[]{0, 0};
    }
}
