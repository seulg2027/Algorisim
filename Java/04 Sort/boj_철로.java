/**
 * 13334번 골드2 철로
 * 시간초과 나지 않기 위해 아이디어가 중요했다..
 */
import java.io.*;
import java.util.*;

public class boj_철로 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        int[][] distance = new int[n][2];

        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            if (s < e) {
                distance[i] = new int[]{s, e};
            } else {
                distance[i] = new int[]{e, s};
            }
        }

        int d = Integer.parseInt(br.readLine());

        // 끝 거리 기준으로 정렬
        // {10, 20}, {10, 25}, {25, 30}, {25, 35}, {5, 40}, {30, 50}, {50, 60}, {80, 100}
        Arrays.sort(distance, (o1, o2) -> o1[1] == o2[1] ? o1[0] - o2[0] : o1[1] - o2[1]);

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int maxValue = 0;
        for (int i=0; i<n; i++) {
            pq.offer(distance[i][0]);
            while (!pq.isEmpty() && pq.peek() < distance[i][1] - d) {
                pq.poll();
            }
            maxValue = Math.max(maxValue, pq.size());
        }

        bw.write(String.valueOf(maxValue) + "\n");
        bw.flush();
        bw.close();
    }
}
