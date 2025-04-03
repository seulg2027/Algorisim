/**
 * 수열
 * 10, 20, 10, 30, 20, 50
 *  1,  2,  1,  3,  2,  4
 */
import java.io.*;
import java.util.*;

public class boj_가장긴증가하는부분수열 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int cnt = 1;

        for (var i = 0; i < n; i++){
            for (var j = 0; j < i; j++) {
                if (arr[j] < arr[i])
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
            }
            cnt = Math.max(dp[i], cnt);
        }
        
        bw.write(String.valueOf(cnt) + "\n");

        bw.flush();
        bw.close();
    }
}
