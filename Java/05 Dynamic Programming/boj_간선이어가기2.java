/**
 * Java로 다익스트라!
 * {{2, 3}, {3, 2}, {4, 4}} // 간선, 가중치
 */
import java.io.*;
import java.util.*;

public class boj_간선이어가기2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<int[]>[] graph = new ArrayList[n+1];
        for (int i=0; i<=n; i++) {
            graph[i] = new ArrayList<int[]>();
        }

        for (int j=0; j<m; j++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a].add(new int[]{b, c});
            graph[b].add(new int[]{a, c});
        }

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st2.nextToken());
        int t = Integer.parseInt(st2.nextToken());

        int[] distance = new int[n+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        distance[s] = 0;
        q.add(new int[]{s, 0}); // 시작 정점, 시작 가중치 0

        while (!q.isEmpty()){
            int[] now = q.poll();
            if (now[1] > distance[now[0]]) {
                continue;
            }
            for (int[] pick : graph[now[0]]) {
                int nextNode = pick[0];
                int cost = pick[1];
                if (distance[nextNode] > cost + now[1]) {
                    distance[nextNode] = cost + now[1];
                    q.add(new int[]{nextNode, distance[nextNode]});
                }
            }
        }
        //System.out.println(Arrays.toString(distance));
        System.out.println(distance[t]);
    }
}
