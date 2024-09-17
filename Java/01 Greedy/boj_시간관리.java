/**
 * 끝내는 시간이 늦은 것부터 거꾸로 계산!
 * 5 20
 * 1 16 (15)
 * 8 14 (14)
 * 3 5 (6) -> 5가 6보다 작으므로, 5로 생각해야 함.
 */
import java.io.*;
import java.util.*;

public class boj_시간관리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] works = new int[N][2]; // 일에 대해 걸리는 시간 / 끝내는 시간
        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            works[i][0] = Integer.parseInt(st.nextToken());
            works[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(works, (o1, o2) -> o1[1] == o2[1] ? o1[0] - o2[0] : o2[1] - o1[1]);
        int lastTime = 0;
        for (int j=0; j<N; j++) {
            if (j == 0) {
                lastTime = works[j][1] - works[j][0];
                continue;
            }
            lastTime = works[j][1] > lastTime ? lastTime : works[j][1];
            lastTime -= works[j][0];
        }

        if (lastTime < 0) lastTime = -1;

        System.out.println(lastTime);
    }
}
