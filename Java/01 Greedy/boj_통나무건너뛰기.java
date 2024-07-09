/**
 * 11497번 실버1 통나무건너뛰기
 */
import java.io.*;
import java.util.*;

public class boj_통나무건너뛰기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            int[] list = new int[N];
            Integer[] trees = Arrays.stream(br.readLine().split(" "))
                                    .mapToInt(Integer::parseInt).boxed().toArray(Integer[]::new);

            Arrays.sort(trees, Collections.reverseOrder());

            int mid;
            if (N % 2 == 0){
                mid = N / 2 - 1;
            } else {
                mid = N / 2;
            }
            for (int i=0; i<N; i++) {
                if (i % 2 == 0){
                    list[mid - i / 2] = trees[i];
                } else {
                    list[mid + (i+1) / 2] = trees[i];
                }
            }

            int maxValue = 0;
            for (int j=0; j<N-1; j++) {
                maxValue = Math.max(maxValue, Math.abs(list[j] - list[j+1]));
            }
            bw.write(String.valueOf(maxValue) + "\n");
        }

        bw.flush();
        bw.close();
    }
}
