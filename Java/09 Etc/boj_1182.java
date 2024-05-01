/**
 * boj_1182
 * 연속된 부분수열의 합
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_1182 {
    static int N, S;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        int[] sequence = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        int sum = 0;
        // 비트마스킹을 이용해 연속된 부분집합 구하기
        for (int i=1; i < (1<<N); i++) {
            sum = 0;
            for (int j=0; j<N; j++) {
                if ((i & (1 << j)) != 0) {
                    sum += sequence[j];
                }
            }
            if (sum == S) answer++;
        }

        System.out.println(answer);
    }
}