/**
 * softeer Lv3 스마트 물류
 */

import java.io.*;
import java.util.*;

public class softeer_스마트물류 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        String[] line = br.readLine().split("");
        boolean[] visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            if ("P".equals(line[i])) {
                for (int j = -K; j <= K; j++) {
                    if (j == 0 || i+j < 0 || i+j >= N) { continue; }

                    if ("H".equals(line[i+j]) && !visited[i+j]){
                        visited[i+j] = true;
                        break;
                    }
                }
            }
        }

        int ans = 0;

        for (boolean v : visited) {
            if (v == true) {ans ++;}
        }

        bw.write(String.valueOf(ans));
        bw.flush();
        bw.close();
    }
}
