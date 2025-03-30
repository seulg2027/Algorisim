/**
 * 그리디 아님.. 배낭문제!
 */
import java.io.*;
import java.util.*;

public class boj_평범한배낭 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        long[][] dp = new long[n + 1][k + 1];
        long maxV = 0;

        for (var i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            for (var j = 0; j < k + 1; j++) {
                if (j < w) dp[i][j] = dp[i-1][j];
                else dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-w] + v);

                maxV = Math.max(maxV, dp[i][j]);
            }
        }

        bw.write(String.valueOf(maxV) + "\n");

        bw.flush();
        bw.close();
    }
}
