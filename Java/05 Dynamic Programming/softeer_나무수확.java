/**
* 인접한 곳 선택 -> 수로 설치 
(n, n) 위치로 가야함, 아래나 오른쪽만 갈 수 있음
1. BFS로 지나가는 길 모두 체크 -> 가장 값이 큰 칸 (시간초과)
2. DP로 체크..
[비용]
2 7 10
5 10 13
13 14 15
*/
import java.io.*;
import java.util.*;

public class softeer_나무수확 {
    public class Main {
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

            int n = Integer.valueOf(br.readLine());
            int[][] graph = new int[n][n];
            int[][] dpN = new int[n][n]; // 스프링쿨러 사용하지 않은 경우
            int[][] dpY = new int[n][n]; // 스프링쿨러 사용한 경우

            for (var i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (var j = 0; j < n; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (var i = 0; i < n; i++) {
                for (var j = 0; j < n; j++) {
                    int up = i != 0 ? dpN[i-1][j] : 0;
                    int left = j != 0 ? dpN[i][j-1] : 0;
                    dpN[i][j] = Math.max(up, left) + graph[i][j]; // 스프링쿨러 사용 X
                    
                    int umax = i != 0 ? Math.max(dpY[i-1][j] + graph[i][j], dpN[i-1][j] + graph[i][j] * 2) : 0;
                    int lmax = j != 0 ? Math.max(dpY[i][j-1] + graph[i][j], dpN[i][j-1] + graph[i][j] * 2) : 0;
                    dpY[i][j] = Math.max(umax, lmax);
                }
            }
            bw.write(String.valueOf(dpY[n-1][n-1]));

            bw.flush();
            bw.close();
        }
    }
}
