/**
 * 바이러스
 */
import java.io.*;
import java.util.*;

public class boj_바이러스_실버3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        ArrayList<Integer>[] computers = new ArrayList[n + 1];
        boolean[] visited = new boolean[n + 1];
        int cnt = 0;

        for (int i = 0; i <= n; i++) {  // 배열 초기화
            computers[i] = new ArrayList<>();
        }

        for (var i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            computers[a].add(b);
            computers[b].add(a);
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        visited[1] = true;

        while (!queue.isEmpty()) {
            int now = queue.poll();
            for (var idx = 0; idx < computers[now].size(); idx++) {
                if (!visited[computers[now].get(idx)]) { // 아직 방문하지 않았다면
                    visited[computers[now].get(idx)] = true;
                    queue.offer(computers[now].get(idx));
                    cnt++;
                }
            }
        }

        bw.write(String.valueOf(cnt) + "\n");

        bw.flush();
        bw.close();
    }
}
