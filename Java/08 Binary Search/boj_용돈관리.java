/**
 * boj_용돈관리
 * 이분탐색 -> 최솟값 구하기
 */
import java.io.*;
import java.util.*;

public class boj_용돈관리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] money = new int[n];
        int minValue = 1, maxValue = 1;

        for (int i = 0; i < n; i++) {
            money[i] = Integer.parseInt(br.readLine());
            minValue = Math.max(minValue, money[i]);
            maxValue += money[i];
        }

        int mid, cnt, sum;

        // 최솟값 구하기
        while (minValue <= maxValue) {
            mid = (minValue + maxValue) / 2;
            sum = 0;
            cnt = 1;

            for (int i=0; i<n; i++) {
                sum += money[i];
                if (sum > mid) { // 넘을 때만 계산
                    sum = money[i]; // 현재 money 가져옴
                    cnt++;
                }
            }
            if (cnt <= m) maxValue = mid-1; // 같으면 계속 줄여나가야함
            else minValue = mid+1;
        }

        bw.write(String.valueOf(minValue));
        bw.flush();
        bw.close();
    }
}