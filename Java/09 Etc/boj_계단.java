/**
 * 투 포인터
 * => 65점 코드
 */
import java.io.*;
import java.util.*;

public class boj_계단 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] histogram = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (var i=0; i<n; i++){
            histogram[i] = Integer.parseInt(st.nextToken());
        }

        int end = 0;
        int maxValue = 0;
        for (var start=0; start < n; start++) {
            int level = 1;
            end = start;
            while (end < n && histogram[end] >= level) {
                end += 1;
                level += 1;
            }
            maxValue = Math.max(maxValue, level-1); // 계단의 최고 높이
        }

        bw.write(String.valueOf(maxValue) + "\n");
        bw.flush();
        bw.close();
    }
}