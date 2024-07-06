
import java.io.*;
import java.util.*;

public class boj_랜선자르기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        
        long[] LANArray = new long[K];
        for (int i=0; i<K; i++) {
            LANArray[i] = Long.parseLong(br.readLine());
        }

        long ans = binarySearch(LANArray, 0, Arrays.stream(LANArray).max().getAsLong(), N);

        bw.write(String.valueOf(ans) + "\n");

        bw.flush();
        bw.close();
    }

    private static long binarySearch(long[] LANArray, long left, long right, int N) {
        while (left <= right) {
            long mid = (left + right) / 2;
            if (mid == 0){ // 0으로 나누는 경우 제외..
                break;
            }
            long LANLen = Arrays.stream(LANArray).map(e -> e / mid).sum(); // 랜선의 길이
            if (LANLen >= N) {
                left = mid + 1;
            } else if (LANLen < N) {
                right = mid - 1;
            }
        }
        return right;
    }
}
