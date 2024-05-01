/**
 * boj_11811
 * 데스스타
 * 비트마스킹
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_11811 {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][N];
        int[] res = new int[N];

        // 2차원 배열 만들면서
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (i == j) continue;

                // OR 연산하기(AND로 연산했으니)
                res[i] |= arr[i][j];
            }
        }

        for (int k=0; k<N; k++) System.out.printf("%d ", res[k]);
    }
}