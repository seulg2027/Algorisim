/**
 * 
 * 10 20 15 25 10 20
 * 10 30 35 55 65 75
 */
import java.io.*;

public class boj_계단오르기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] stairs = new int[n];
        for (var i = 0; i < n; i++) {
            stairs[i] = Integer.parseInt(br.readLine());
        }

        int[] dp = new int[n];
        dp[0] = stairs[0];
        if (n >= 2) {
            dp[1] = dp[0] + stairs[1];
        }

        for (var i = 2; i < n; i++) {
            if (i >= 3) {
                dp[i] = stairs[i] + Math.max(dp[i - 2], stairs[i - 1] + dp[i - 3]);
            } else {
                dp[i] = stairs[i] + Math.max(dp[i - 2], stairs[i - 1]);
            }
        }

        bw.write(String.valueOf(dp[n - 1]) + "\n");

        bw.flush();
        bw.close();
    }
}
