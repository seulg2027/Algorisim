/**
 * softeer Lv3 징검다리
 */

import java.io.*;
import java.util.*;

public class softeer_징검다리 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] dp = new int[n];

        for (int i=0; i<n; i++) {
            int maxValue = 0;
            for (int j=0; j<i; j++) {
                if (array[j] < array[i]) {
                    maxValue = Math.max(maxValue, dp[j]);
                }
            }
            dp[i] = maxValue + 1;
        }
        
        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}
