/**
 * 높이 구간에 따라 장애물 파괴
 * [석순]
 * {1, 0, 1, 0, 1, 0, 0}
 * {3, 2, 2, 1, 1, 0, 0}
 * 
 * [종유석]
 * {0, 0, 1, 0, 1, 0, 1}
 * {0, 0, 1, 1, 2, 2, 3}
 * 
 * -> {3, 2, 3, 2, 3, 2, 3}
 */
import java.io.*;
import java.util.*;

public class boj_개똥벌레 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        int[] sg = new int[h];
        int[] sc = new int[h];

        for (var i = 0; i < n; i++) {
            int height = Integer.parseInt(br.readLine());
            if (i % 2 == 0) { // 석순
                sg[height - 1] += 1;
            } else { // 종유석
                sc[h - height] += 1;
            }
        }

        for (var j = h-2; j >= 0; j--) {
            sg[j] += sg[j + 1];
        }
        for (var z = 1; z <= h-1; z++) {
            sc[z] += sc[z - 1];
        }

        int[] results = new int[h];
        for (var x = 0; x < h; x++) {
            results[x] = sg[x] + sc[x];
        }

        Arrays.sort(results);
        bw.write(String.valueOf(results[0]) + " " + Arrays.stream(results).filter(i -> i == results[0]).count() + "\n");

        bw.flush();
        bw.close();
    }
}
